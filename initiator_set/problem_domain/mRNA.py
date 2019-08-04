


class mRNA :
	
	def __init__(self,cd:str,og:str,pal:int):
		
		self.code: str = cd
		self.originGene:str = og
		self.polyALength:int = pal
		
		self.baseWeights:list[float] = []
		self.kozakStrengths:list[float] = []
		self.leakyScanStrengths:list[float] = []
		
		self.localisationSequences:list[tuple] = []
		self.hairpins:list[tuple] = []
		self.IREs:list[tuple] = []
		self.uORFs:list[tuple] = []
		
		
		self.adjustedWeights:list[float] = []
		self.processedBy:list[str] = []
		
	

class Iterable(codonString) :

	def __init__(self, parent:mRNA, start:int, stop:int):

		self.parent:mRNA = parent
		self.loc:int = start
		self.stop:int = stop


	def __iter__(self):
		return self


	def next(self):
		if self.loc >= stop:
			raise StopIteration
		
		value = parent.code[self.loc:(self.loc + 2)]
		self.loc += 3
		return value
