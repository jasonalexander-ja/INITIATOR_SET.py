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
	m_weights = open(mypath + "/codonWeights.dat", "rb")
except OSError as e:
	print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
		, file=sys.stderr)
	raise



def mapAICs(rna:mRNA.mRNA) -> mRNA.mRNA:

	for i in rna.code:
		m_weights.seek(i * 8)
		rna.baseWeights.append(unpack('<d', m_weights.read(8))[0])

	return rna
