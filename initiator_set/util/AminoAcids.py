# AminoAcids.py
# 
# Utils for dealing with Amino Acid Chains
#
# Authored by: Lucianna Osucha (email:lucianna@vulpinedesigns.com)



from mRNA import *



const aminoAlphabet:str = '*RHKDESTNQCUGPAVILMFYW'
const aminoCodons:list = [3, 8, 3, 8, 16, 16, 18, 16, 1, 6, 1, 6, 7, 7, 7, 7, 0, 20
	, 0, 20, 17, 19, 17, 19, 0, 10, 21, 10, 6, 6, 6, 6, 5, 4, 5, 4, 15, 15, 15
	, 15, 12, 12, 12, 12, 14, 14, 14, 14, 9, 2, 9, 2, 17, 17, 17, 17, 1, 1, 1, 1
	, 13, 13, 13, 13]



class AminoAcidChain:
	def __init__(self, seq:list[int]):
		self.sequence:list[int] = seq
		self.length:int = len(seq)
		self.postTranslationalModificationSites:list = []
		
	
	
	def __init__(self, seq:str):
		self.__init__([aminoAlphabet.index(i) for i in seq])
