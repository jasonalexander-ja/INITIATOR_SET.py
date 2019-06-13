class AminoAcidChain:
	def __init__(self,seq:str):
		self.sequence:str = seq
		self.length:int = len(seq)
		self.postTranslationalModificationSites:list[tuple] = []
		