########################################################################################################################
#
# This file supports interpreting Kozak Consensus Sequences from file and constructing them into KzConsensus instances
# It is recommended to use these methods to construct KzConsensus instances due to the difficulty of
# describing the analogue nature of Kozak Consensus Sequences.
#
# See sample_kozaks.txt for the syntax structure of a kozak file
#
########################################################################################################################

# import sys
# sys.path.append('E:\\Documents\\Volunteer\\VulpineDesign\\INITIATOR_SET-master\\initiator_set')
from typing import *
from io import StringIO
from kozak_calculator.kozak_consensus import *


# Given an input file or something, construct whatever is in it into a
# collection of KzConsensus instances
def interpret_kozak_file(datafile: StringIO, filename="") -> List[KzConsensus]:
    result: List[KzConsensus] = []
    last_line_was_terminated = False

    try:
        while True:
            line = datafile.readline()
            if line is None or line == "":
                if last_line_was_terminated:
                    break
                else:
                    last_line_was_terminated = True
            line = remove_comments(line)
            if line is None or line == "":
                continue
            spl = line.split(":")
            if line.count(":") == 1 and len(spl) > 1:
                result.append(interpret_kozak_consensus(datafile, spl[0]))
                # print(spl)
    except ValueError:
        errormsg = "Cannot parse data."
        if filename != "":
            errormsg += " Misunderstood file " + filename
        raise ValueError(errormsg)

    # print(result)
    return result


# Simply translates an initiator codon string (e.g "AUG")
# into a list of KzNucleotide instances representing the codon
def codon_of(initiator_codon: str) -> List[KzNucleotide]:
    result: List[KzNucleotide] = []
    for c in initiator_codon.lower():
        a1 = 1 if c == 'a' else 0
        u1 = 1 if c == 'u' else 0
        g1 = 1 if c == 'g' else 0
        c1 = 1 if c == 'c' else 0

        # Initiator codon KzNucleotide instances get an importance value of -1
        kzn = KzNucleotide(a=a1, u=u1, g=g1, c=c1, importance=-1)
        result.append(kzn)

    return result


# Given an input file or something, construct a KzConsensus instance out of the file
# in retrospect to the file syntax as described in sample_kozaks.txt
def interpret_kozak_consensus(datafile: StringIO, initiator_codon: str) -> KzConsensus:
    result = KzConsensus(sequence=[], codonStart=0)

    i = 0
    while True:
        line = datafile.readline()

        # End consensus with new line
        if line is None or line.isspace() or line == "":
            return result

        # Comments with #
        line = remove_comments(line).strip()
        if line.isspace() or line == "":
            continue  # Ignore lines that were comments

        # Specify initiator codon with -
        if line.find('-') > -1:
            result.codonStart = i
            result.sequence.extend(codon_of(initiator_codon))
        elif line.find('conserved >= ') > -1:
            result.conserved_threshold = float(line.split('conserved >=')[1])
        elif line.find('homologous >= ') > -1:
            result.conserved = float(line.split('homologous >=')[1])
        else:
            # Build KzNucleotide with (f f f f i)
            kzn: KzNucleotide = interpret_kozak_weights(line)
            i = i + 1
            result.sequence.append(kzn)

        pass

    if result.conserved_threshold < 0 or result.similarity_threshold:
        raise ValueError("Missing threshold values ([] >= #)")
    if not result.conserved:
        raise ValueError("No conserved threshold (could be treated as >0? just put it in though.)")
    return result


# Construct, from a weights entry from a string, a KzNucleotide object with its data
# e.g "0.24 0.24 0.28 0.24 1"
def interpret_kozak_weights(line: str) -> KzNucleotide:
    values: List[str] = line.split(" ")
    if len(values) != 5:
        raise ValueError("Malformed weight line")
    try:
        result = KzNucleotide(a=float(values[0]), u=float(values[1]), g=float(values[2]), c=float(values[3]),
                              importance=int(values[4]))
        return result
    except ValueError as e:
        raise ValueError("Malformed weight value")


# Ignore any comments with the parser
def remove_comments(line: str):
    return line.split("#")[0]
