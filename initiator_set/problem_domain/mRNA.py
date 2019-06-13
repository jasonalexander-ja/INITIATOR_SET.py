class mRNA :
	
	def __init__(self,cd:str,og:str,pal:int):
		
		self.code: str = cd
		self.originGene:str = og
		self.polyALength:int = pal
		
		self.kozakStrengths:list[float] = []
		self.leakyScanStrengths:list[float] = []
		
		self.localisationSequences:list[tuple] = []
		self.hairpins:list[tuple] = []
		self.IREs:list[tuple] = []
		self.uORFs:list[tuple] = []
		
		self.processedBy:list[str] = []
		
	
	def getReadingFrame(self,start:int) -> str:
		return self.code[start:]
	