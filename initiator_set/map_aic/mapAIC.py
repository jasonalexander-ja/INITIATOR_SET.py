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



def rankWeight(list_, weight, index):
	for i in range(0, len(list_)):
		if weight > list_[1]:
			list_.insert(i, (index, weight))
	i.append((index, weight))



def rankWeight(list_, weight, index):
	for i in range(0, len(list_)):
		if weight > list_[1]:
			list_.insert(i, (index, weight))
	i.append((index, weight))


def mapAICs(rna:mRNA.mRNA) -> mRNA.mRNA:
	rna.metadata["baseWeights"] = []
	rna.metadata["baseWeightsOrdered"] = []

	for i in rna.code:
		# Go to the desired entry in datafile
		m_weights.seek(i * 4)
		weight = unpack('<f', m_weights.read(4))[0]
		rna.metadata["baseWeights"].append(weight)
		rankWeight(rna.metadata["baseWeightsOrdered"], weight, i)

	return rna
