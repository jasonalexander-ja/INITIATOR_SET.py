# mRNA.py
#
# A representation of mRNA strand with a slew of metadata and utils for working
# with it
#
# Authored by: Lucianna Osucha (lucianna@vulpinedesigns.com)



bases = ['A', 'U', 'G', 'C'];



def deindexCodon(index:int) -> str:
  result = bases[int(index/16)]
  result += bases[int((index/4))%4]
  result += bases[index%4]
  return result



def deindexRNA(code:list) -> str:
  result = ''
  for i in range (0, len(code), 3):
    result = result + codonIndex(code[i])

  i = len(code) % 3
  result = result[:-i] + codonIndex(code[-1])
  return result



def indexCodon(codon:str) -> int:
  result = bases.index(codon[0]) * 16
  result += bases.index(codon[1]) * 4
  result += bases.index(codon[2])
  return result



def indexRNA(code:str) -> list:
  result = []
  for i in range(len(code) - 2):
    result.append(indexCodon(code[i:i+3]))
  return result



class mRNA:


  def __init__(self, cd):
    if isinstance(cd, str):
      cd = indexRNA(cd)
    if not isinstance(cd, list):
      raise TypeError("'cd' must be of type 'str' or 'list'")

    self.code:list = cd

    # DEPRECATED! USE METADATA DICT INSTEAD!!!!!
    self.baseWeights:list = []
    self.adjustedWeights:list = []
    # ^^^^^^^^^^^^ DEPRECATED ^^^^^^^^^^^^^^^^^^

    self.metadata:dictionary = {}



  def __str__(self) -> str:
    return rnaIndex(self.code) + "\n\n" + self.metadata

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
