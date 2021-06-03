# mapAIC.py
#
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (lucianna@vulpinedesigns.com)
from io import FileIO
import sys
import os
from typing import Callable

from util import mRNA
from struct import unpack


# try:
#     m_weights = open(mypath + os.sep + "codonWeights.dat", "rb")  # rb = read bytecode
# except OSError as e:
#     print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
#           , file=sys.stderr)
#     raise

# Maps Initiation Codon probability over an mRNA instance.
# Usage example:
# print(mapAICs(mRNA.mRNA("AUGGGGCUG")))
def mapAICs(rna: mRNA.mRNA,
            filepath: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "codonWeights.dat")) -> mRNA.mRNA:
    m_weights = open(filepath, "rb")
    rna.metadata["baseWeights"] = []
    for i in rna.code:
        # Go to the desired entry in datafile
        m_weights.seek(i * 4)
        weight = unpack('<f', m_weights.read(4))[0]
        rna.metadata["baseWeights"].append(weight)

    # Calculate adjusted weights
    # I saw this entry was lying around in the original map AIC but not calculated
    # I'm taking it as normalising the weights so that all values are between 0 and 1
    # Where 1.0 was whatever the maximum weighted entry previously was
    # Probably not even needed

    # Find max weight
    w_max = 0
    for i in rna.metadata["baseWeights"]:
        if i > w_max:
            w_max = i

    adjusted_weights = []
    for i in rna.metadata["baseWeights"]:
        try:
            adjusted_weights.append(i / w_max)
        except ZeroDivisionError:
            adjusted_weights.append(0)
    rna.metadata['adjusted_weights'] = adjusted_weights

    return rna


# taken from https://www.arduino.cc/en/Reference/Map
def rangeScale(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#
def floatToFastQScore(score: float, min: float = 0.0, max: float = 1.0) -> str:
    """
    :param min: minimum possible score value (default 1.0)
    :param max: maximum possible score value (default 1.0)
    :return: score translated into the numbering system (order lowest->highest):
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    """
    return chr(int(rangeScale(score, 0.0, max, 33, 126)))


# This can possibly be generalised in the mRNA.mRNA class if we standardise quality scores across projects
# Some might not so we would want some way of telling which can be generalised or not.
# It appears some other biology software uses nonlinear quality scores
# https://en.wikipedia.org/wiki/FASTQ_format#Variations
# so this method will externalise whatever scoring system.
# By default though it's linear-rounding across the default FASTQ quality scoring alphabet.
# note that any floats in the function below are 0.0 < x < 1.0
def fastQScoreAICs(rna: mRNA.mRNA, qualityAdjustment: Callable[[float], str] = floatToFastQScore) -> str:
    return "".join([qualityAdjustment(x) for x in rna.metadata["adjusted_weights"]])


def aicsToFastQ(rna: mRNA.mRNA):
    return(
        "@Alternative Initiation Codon Possibilities for (sequence of length "+str(len(rna.code))+")\n" +
        rna.deindexRNA() +
        "\n+\n" +
        fastQScoreAICs(rna))

# test function
def outputAICsAsFastQ(rna: mRNA.mRNA,
                      output: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test-aics-fastq.fq")):
    with open(output, 'w') as file:
        file.write(aicsToFastQ(rna))


# print(chr(ord('A') + 1))
mrt = mRNA.mRNA("AUGCGGGCCC")
mrt.metadata = {}
mapAICs(mrt)
# print(fastQScoreAICs(mrt))
# print(aicsToFastQ(mrt))
outputAICsAsFastQ(mrt)