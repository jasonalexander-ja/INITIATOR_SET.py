# AminoAcids.py
# 
# Utils for dealing with Amino Acid Chains
#
# Authored by:
# Coauthored by: Lucianna Osucha (email:lucianna@vulpinedesigns.com)


const aminoAlphabet = "KNKNIIMIRSRSTTTT*Y*YLFLF*CWCSSSSEDEDVVVVGGGGAAAAQHQHLLLLRRRRPPPP"

class AminoAcidChain:
	def __init__(self,seq:str):
		self.sequence:str = seq
		self.length:int = len(seq)
		self.postTranslationalModificationSites:list[tuple] = []
		
