# AminoAcids.py
#
# Utils for dealing with Amino Acid Chains along with a class to represent them
#
# Authored by: Lucianna Osucha (lucianna@vulpinedesigns.com)


import mRNA


# What codon indexes from AAA-CCC will translate into
aminoCodons = "KNKNIIMIRSRSTTTT*Y*YLFLF*CWCSSSSEDEDVVVVGGGGAAAAQHQHLLLLRRRRPPPP"


# Take a coding sequence and return the Amino Acid Chain it will translate into
def convertRNA(seq:list, stcodon =0) -> list:
	result:list = []
	for i in range(0, len(seq), 3):
		amino = aminoCodons[seq[i]]
		if (amino == '*')
			break
		result.append(amino)
	return result




class AminoAcidChain:
	# Instantiates a new AminoAcidChain object using plain text
	def __init__(self, seq:string):
		self.sequence:string = seq
		self.length:int = len(seq)

		self.metadata:list = []


	# Takes
	# an mRNA object, a string of RNA in plain text, or an RNA index list
	# and
	# the codon index to begin reading from
	# and returns a new AminoAcidChain
	@classmethod
	def fromCodingSequence(cls, seq, stcodon =0):
		if isinstance(seq, mRNA.mRNA):
			seq = seq.code
		if isinstance(seq, str):
			seq = indexRNA(seq)
		if isinstance(seq, list):
			return cls(convertRNA(seq, stcodon))
		else:
			raise TypeError("'seq' must be of type 'mRNA', 'str', or 'list'")


	def __str__(self) -> str:
		return self.sequence + "\n\n" + self.metadata
