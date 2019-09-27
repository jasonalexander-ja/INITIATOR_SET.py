# mapAIC.py
# 
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)

import sys
sys.path.append('../')
from util.mRNA import *
from struct import *



try:
	m_weights = open("codonWeights.dat", "rb") 
except OSError as e:
	print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
		, file=sys.stderr)
	raise



def mapAICs(rna:mRNA) -> mRNA:
	
	for i in rna.code:
		m_weights.seek(i * 8)
		rna.baseWeights.append(unpack('<d', m_weights.read(8)))

	return rna
