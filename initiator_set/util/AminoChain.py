# AminoAcids.py
#
# Utils for dealing with Amino Acid Chains
#
# Authored by: Lucianna Osucha (lucianna@vulpinedesigns.com)



import mRNA


metadataTypes:list = ['originMRNA', 'locFlags']
aminoAlphabet:list = ['*', 'R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U', 'G'
	, 'P', 'A', 'V', 'I', 'L', 'M', 'F', 'Y', 'W']
aminoCodons:list = [3, 8, 3, 8, 16, 16, 18, 16, 1, 6, 1, 6, 7, 7, 7, 7, 0, 20
	, 0, 20, 17, 19, 17, 19, 0, 10, 21, 10, 6, 6, 6, 6, 5, 4, 5, 4, 15, 15, 15
	, 15, 12, 12, 12, 12, 14, 14, 14, 14, 9, 2, 9, 2, 17, 17, 17, 17, 1, 1, 1, 1
	, 13, 13, 13, 13]


def indexAminoChain(seq:str) -> list:
	result:list = []
	for i in seq:
		result.append(aminoAlphabet.index(i))
	return result



def deindexAminoChain(seq:list) -> str:
	result = '';
	for i in seq:
		result += aminoAlphabet[i]
	return result;



def convertRNA(seq:list) -> list:
	result:list = []
	for i in range(0, len(seq), 3):
		result.append(aminoCodons[seq[i]])
	return result




class AminoAcidChain:
	def __init__(self, seq):
		self.metadata:list = []

		if isinstance(seq, str):
			seq = indexAminoChain(seq)
		if isinstance(seq, list):
			self.sequence:list[int] = seq
		else:
			raise TypeError("'seq' must be of type 'str' or 'list'")
		self.length:int = len(seq)


	@classmethod
	def fromMRNA(cls, seq):
		if isinstance(seq, mRNA.mRNA):
			seq = seq.code
		if isinstance(seq, str):
			seq = indexRNA(seq)
		if isinstance(seq, list):
			print(seq)
			return cls(convertRNA(seq))
		else:
			raise TypeError("'seq' must be of type 'mRNA', 'str', or 'list'")


	def __str__(self) -> str:
		return deindexAminoChain(self.sequence)
