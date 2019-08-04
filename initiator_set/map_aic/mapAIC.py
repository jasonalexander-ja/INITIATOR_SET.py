# mapAIC.py
# 
# Reads weights from a file, maps them to codons in arbitrary
# strings of mRNA
#
# Author email: foul-fortune-feline@pm.me

import sys
sys.path.append('../')
from problem_domain.mRNA import *



## codonWeighting.dat is a file filled with float data end to end
## from AAA - UUU - GGG - CCC
try:
	weights = open("codonWeighting.dat", "rb") 
except OSError as e:
	print("Error opening \"codonWeighting.dat\"", file=sys.stderr)
	raise



def indexCodon(codon:str) -> int:  # Indexing elifant
	result:int
	
	if   codon[0] == "A":
		result = 0
	elif codon[0] == "U":
		result = 16 
	elif codon[0] == "G":
		result = 32
	elif codon[0] == "C":
		result = 48
		
	if   codon[1] == "A":
		result += 0       	
	elif codon[1] == "U":
		result += 4 
	elif codon[1] == "G":
		result += 8
	elif codon[1] == "C":
		result += 12
	
	if   codon[2] == "A":
		result += 0       	
	elif codon[2] == "U":
		result += 1
	elif codon[2] == "G":
		result += 2
	elif codon[2] == "C":
		result += 3
		
	return result



def mapAICs(rna:mRNA) -> mRNA:
	for i in range(len(rna.code)):
		index = indexCodon(rna.code[i])
		rna.baseWeights[i] = weights[index*400]

	return mRNA
