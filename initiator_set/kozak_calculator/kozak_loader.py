from typing import *
from io import StringIO
from initiator_set.kozak_calculator.kozak_calculator import *

__lineno = 0

def interpret_kozak_file(datafile: StringIO) -> List[KzConsensus]:
    result: List[KzConsensus] = []
    last_line_was_terminated = False
    global __lineno
    __lineno = 0
    try:
        while True:
            line=datafile.readline()
            if line is None or line == "":
                if last_line_was_terminated:
                    break
                else:
                    last_line_was_terminated = True
            line = remove_comments(line)
            spl = line.split(":")
            if line.count(":") == 1 and len(spl) > 1:
                result.append(interpret_kozak_consensus(datafile, spl[0]))
            __lineno = __lineno + 1
    except:
        raise ValueError("Cannot parse data as kozak consensus")

    return result


def codon_of(initiator_codon: str) -> List[KzNucleotide]:
    result: List[KzNucleotide] = []
    for c in initiator_codon.upper():
        a1 = 1 if c == 'A' else 0
        u1 = 1 if c == 'U' else 0
        g1 = 1 if c == 'G' else 0
        c1 = 1 if c == 'C' else 0

        kzn = KzNucleotide(a=a1,u=u1,g=g1,c=c1,importance=0)
        result.append(kzn)

    return result


def interpret_kozak_consensus(datafile: StringIO, initiator_codon: str) -> KzConsensus:
    result = KzConsensus(sequence=[], codonStart = 0)
    global __lineno
    try:
        i = 0
        while True:
            line=datafile.readline()

            # End consensus with new line
            if line is None or line.isspace() or line == "":
                return result

            # Comments with #
            line = remove_comments(line).strip()
            if line.isspace() or line == "":
                continue  # Ignore lines that were comments

            # Specify initiator codon with -
            if line.find('-') > -1:
                result.codonStart = __lineno
                result.sequence.extend(codon_of(initiator_codon))
            else:
                # Build KzNucleotide with (f f f f i)
                kzn: KzNucleotide = interpret_kozak_weights(line)
                result.sequence.append(kzn)

            i = i + 1
            pass

            __lineno = __lineno + 1
        pass
    except:
        raise ValueError("Cannot parse data as kozak consensus")


def interpret_kozak_weights(line: str) -> KzNucleotide:
    values: List[str] = line.split(" ")
    if len(values) != 5:
        raise ValueError("Malformed weight line")
    try:
        result = KzNucleotide(a=float(values[0]),u=float(values[1]),g=float(values[2]),c=float(values[3]),importance=int(values[4]))
        return result
    except ValueError as e:
        raise ValueError("Malformed weight value")


def remove_comments(line: str):
    return line.split("#")[0]