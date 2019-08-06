# mapAIC.py
# 
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)

import sys
sys.path.append('../')
from util.mRNA import *
from struct import *


bases = ['A', 'U', 'G', 'C'];



def codonIndex(index:int) -> str:
	result = bases[int(index/16)]
	result += bases[int((index/4))%4]
	result += bases[index%4]
	return result



def indexCodon(codon:str) -> int:
	result = bases.index(codon[0]) * 16
	result += bases.index(codon[1]) * 4
	result += bases.index(codon[2])
		
	return result



def mapAICs(rna:mRNA) -> mRNA:
	try:
		m_weights = open("codonWeights.dat", "rb") 
	except OSError as e:
		print("[!!FATAL!!] Error opening \"codonWeights.dat\"\n"
			, file=sys.stderr)
		raise
	
	for i in range(0, len(rna.code) - 2):
		index = indexCodon(rna.code[i:i+3])
		m_weights.seek(index * 8)
		rna.baseWeights.append(unpack('<d', m_weights.read(8)))

	return mRNA
