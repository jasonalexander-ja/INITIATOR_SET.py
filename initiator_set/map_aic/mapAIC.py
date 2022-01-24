# mapAIC.py
#
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (lucianna@vulpinedesigns.com)
from io import FileIO
import sys
import os
from util import mRNA
from struct import unpack, pack
from util.mRNA import indexCodon


# try:
#     m_weights = open(mypath + os.sep + "codonWeights.dat", "rb")  # rb = read bytecode
# except OSError as e:
#     print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
#           , file=sys.stderr)
#     raise

def addCodonWeights(rna: mRNA.mRNA, codon, weights) -> mRNA.mRNA:
    # rna.Metadata
    # Find max weight
    w_max = 0
    for i in rna.Metadata["baseWeights"]:
        if i > w_max:
            w_max = i

    adjusted_weights = []
    for i in rna.Metadata["baseWeights"]:
        try:
            adjusted_weights.append(i / w_max)
        except ZeroDivisionError:
            adjusted_weights.append(0)
    rna.Metadata['adjustedWeights'] = adjusted_weights

    return rna

def mapAICs(rna: mRNA.mRNA, weights) -> mRNA.mRNA:
    rna.Metadata["baseWeights"] = []
    for i in rna.Code:
        rna.Metadata["baseWeights"].append(weights[i])
    # Calculate adjusted weights
    # I saw this entry was lying around in the original map AIC but not calculated
    # I'm taking it as normalising the weights so that all values are between 0 and 1
    # Where 1.0 was whatever the maximum weighted entry previously was
    # Probably not even needed

    # Find max weight
    w_max = 0
    for i in rna.Metadata["baseWeights"]:
        if i > w_max:
            w_max = i

    adjusted_weights = []
    rna.Metadata['adjustedWeights'] = []
    for i in rna.Metadata["baseWeights"]:
        try:
            adjusted_weights.append(i / w_max)
        except ZeroDivisionError:
            adjusted_weights.append(0)
    rna.Metadata['adjustedWeights'] = adjusted_weights

    return rna
#
# def mapAICs(rna: mRNA.mRNA,
#             filepath: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "codonWeights.dat")) -> mRNA.mRNA:
#     rna.Metadata["baseWeights"] = []
#     try:
#         with open(filepath, "rb") as m_weights:
#             for i in rna.Code:
#             # Go to the desired entry in datafile
#                 m_weights.seek(i * 4)
#                 weight = unpack('<f', m_weights.read(4))[0]
#                 rna.Metadata["baseWeights"].append(weight)
#     except OSError as e:
#         print("Cannon open codonWeights.dat file, ", e)
#     # Calculate adjusted weights
#     # I saw this entry was lying around in the original map AIC but not calculated
#     # I'm taking it as normalising the weights so that all values are between 0 and 1
#     # Where 1.0 was whatever the maximum weighted entry previously was
#     # Probably not even needed
#     # Find max weight
#     w_max = 0
#     for i in rna.Metadata["baseWeights"]:
#         if i > w_max:
#             w_max = i
#     adjusted_weights = []
#     for i in rna.Metadata["baseWeights"]:
#         try:
#             adjusted_weights.append(i / w_max)
#         except ZeroDivisionError:
#             adjusted_weights.append(0)
#     rna.Metadata['adjustedWeights'] = adjusted_weights
#     return rna


def loadCodonWeightsFromInputFile(inputFile,
                                  weightFileName: str = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                     "codonWeights.dat")) -> list:
    try:
        weights = [0.00] * 64
        while True:
            codon = inputFile.read(4)
            if codon is None or codon == "":
                break
                # Comments with #
            isCommentLine = codon.split("#")[0].strip()
            if isCommentLine.isspace() or isCommentLine == "":
                continue  # Ignore lines that were comments

            weights[indexCodon(codon)] = float(inputFile.readline())
    except ValueError as e:
        raise e

    # write the new weights (that are now in memory, overwrite the whole file)
    try:
        with open(weightFileName, '+wb') as weightFile:
            for i in weights:
                weightFile.write(bytearray(pack('<f', i)))
    except OSError as e:
        print("Cannot open codonWeights.dat file. " + e)
    # Print out success message
    # print("codonWeights.dat file updated. Run without arguments to verify changes")

    # Find max weight
    w_max = 0
    for i in weights:
        if i > w_max:
            w_max = i

    adjusted_weights = [0.00]*64
    for i in range(0, len(weights)):
        try:
            adjusted_weights[i] = weights[i] / w_max
        except ZeroDivisionError:
            adjusted_weights[i] = 0.00

    return weights, adjusted_weights
