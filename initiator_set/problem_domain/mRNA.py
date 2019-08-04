


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
		
	

class Iterable(mRNA) :

	def __init__(self, parent:mRNA, start:int, stop:int):

		self.parent:mRNA = parent
		self.loc:int = start - 3
		if stop <= start or stop > len(parent.code):
			self.stop = len(parent.code)
		else:
			self.stop:int = stop


	def __iter__(self):
		return self


	def next(self):
		self.loc += 3
		if self.loc >= self.stop:
			raise StopIteration
		
		value = self.parent.code[self.loc:(self.loc + 3)]
		return value
