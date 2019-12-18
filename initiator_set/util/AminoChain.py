# AminoAcids.py
#
# Utils for dealing with Amino Acid Chains
#
# Authored by: Lucianna Osucha (lucianna@vulpinedesigns.com)



import mRNA


metadataTypes:list = ['originMRNA', 'locFlags']
aminoAlphabet:list = ['*', 'R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U', 'G'
	, 'P', 'A', 'V', 'I', 'L', 'M', 'F', 'Y', 'W']
# All codons from AAA-CCC and the Amino Acid index (in aminoAlphabet) they point to
aminoCodons:list = [3, 8, 3, 8, 16, 16, 18, 16, 1, 6, 1, 6, 7, 7, 7, 7, 0, 20
	, 0, 20, 17, 19, 17, 19, 0, 10, 21, 10, 6, 6, 6, 6, 5, 4, 5, 4, 15, 15, 15
	, 15, 12, 12, 12, 12, 14, 14, 14, 14, 9, 2, 9, 2, 17, 17, 17, 17, 1, 1, 1, 1
	, 13, 13, 13, 13]


# Take a plain text Amino Acid Chain and return a list of the indexed form
def indexAminoChain(seq:str) -> list:
	result:list = []
	for i in seq:
		result.append(aminoAlphabet.index(i))
	return result


# Take an indexed Amino Acid Chain and return a list of the plain text form
def deindexAminoChain(seq:list) -> str:
	result = '';
	for i in seq:
		result += aminoAlphabet[i]
	return result;


# Take a string of RNA and return the Amino Acid Chain (in index form) it
# will translate into
def convertRNA(seq:list) -> list:
	result:list = []
	for i in range(0, len(seq), 3):
		result.append(aminoCodons[seq[i]])
	return result




class AminoAcidChain:
	# Instantiates a new AminoAcidChain object using either plain text or
	# preindexed input
	def __init__(self, seq):
		self.metadata:list = []

		if isinstance(seq, str):
			seq = indexAminoChain(seq)
		if isinstance(seq, list):
			self.sequence:list[int] = seq
		else:
			raise TypeError("'seq' must be of type 'str' or 'list'")
		self.length:int = len(seq)


	# Converts an mRNA object, a string of RNA in plain text, or an RNA
	# index list, to a new aminoAcidChain
	@classmethod
	def fromMRNA(cls, seq):
		if isinstance(seq, mRNA.mRNA):
			seq = seq.code
		if isinstance(seq, str):
			seq = indexRNA(seq)
		if isinstance(seq, list):
			return cls(convertRNA(seq))
		else:
			raise TypeError("'seq' must be of type 'mRNA', 'str', or 'list'")


	def __str__(self) -> str:
		return deindexAminoChain(self.sequence)
