# mapAIC.py
#
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (lucianna@vulpinedesigns.com)
from io import FileIO
import sys
import os
from util import mRNA
from struct import unpack

# try:
#     m_weights = open(mypath + os.sep + "codonWeights.dat", "rb")  # rb = read bytecode
# except OSError as e:
#     print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
#           , file=sys.stderr)
#     raise


def mapAICs(rna: mRNA.mRNA, filepath: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "codonWeights.dat")) -> mRNA.mRNA:
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
