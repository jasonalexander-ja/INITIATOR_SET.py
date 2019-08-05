# mapAIC.py
# 
# Reads weights from a file, maps them to codons in arbitrary strings of mRNA
#
# Author email: foul-fortune-feline@pm.me

import sys
sys.path.append('../')
from problem_domain.mRNA import *
from struct import *



def indexBase(base:str) -> int:
	if   base[0] == 'A':
		return 0       	
	elif base[0] == 'U' or base[0] == 'T':
		return 1
	elif base[0] == 'G':
		return 2
	elif base[0] == 'C':
		return 3



def baseIndex(index:int) -> str:
	if   index == 0:
		return 'A'
	elif index == 1:
		return 'U'
	elif index == 2:
		return 'G'
	elif index == 3:
		return 'C'



def codonIndex(index:int) -> str:
	result = baseIndex(int(index/16))
	result += baseIndex(int((index/4))%4)
	result += baseIndex(index%4)
	return result



def indexCodon(codon:str) -> int:
	result = indexBase(codon[0]) * 16
	result += indexBase(codon[1]) * 4
	result += indexBase(codon[2])
		
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
