# mapAIC.py
#
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (lucianna@vulpinedesigns.com)


from __init__ import *
import sys
from util import mRNA
from struct import *



try:
	m_weights = open(mypath + "/codonWeights.dat", "rb") # rb = read bytecode
except OSError as e:
	print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
		, file=sys.stderr)
	raise


def mapAICs(rna:mRNA.mRNA) -> mRNA.mRNA:
	rna.metadata["baseWeights"] = []

	for i in rna.code:
		# Go to the desired entry in datafile
		m_weights.seek(i * 4)
		weight = unpack('<f', m_weights.read(4))[0]
		rna.metadata["baseWeights"].append(weight)

	return rna
