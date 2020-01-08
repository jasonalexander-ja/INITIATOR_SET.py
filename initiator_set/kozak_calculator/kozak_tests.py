import kozak_calculator
from kozak_calculator import *

# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

# arguments are like A, U, G, C
# print(KzNucleotide(.5,.5,0,0).__str__())
# print(KzNucleotide(1,0,0,0).__str__())
# print(KzNucleotide(1,0,0,0).__str__())
# print(KzNucleotide(1,0,0,0).__str__())
# print(KzNucleotide(0,0,1,1).__str__())
# print(KzNucleotide(.5,0,0.5,0).__str__())
# print(KzNucleotide(.25,.25,.25,.25).__str__())
# print(KzNucleotide(.25,.25,.25,.25).__str__())
# print(KzNucleotide(.33,.25,.25,.18).__str__())
# print(KzNucleotide(.18,.25,.25,.33).__str__())
# print(KzNucleotide(.25,.251,.25,.249).__str__())
# print(KzNucleotide(.25,.251,.25,.249).dominants())
# print(KzNucleotide(.5,0,0.5,0).__str__())

# nt1 = KzNucleotide(.25,.251,.25,.249)
# nt2 = KzNucleotide(.5,.5,0,0)
# nt3 = KzNucleotide(.25,.25,.25,.25)
# nt4 = KzNucleotide(1,0,0,0)
#
# I'm not sure how to include factors
# but basically they represent bits in a sequence logo diagram, where bits of great value are conserved
# i still don't understand how to read these diagrams though so for now I just have my own arbitrary conservation judgement process based off distribution
# c1 = KzConsensus(strength=1, codonStart=3, sequence=[nt1, nt2, nt3, nt4,nt1, nt2, nt3, nt4,nt1, nt2, nt3, nt4,nt1, nt2, nt3, nt4]) #, factors=[0.1, 0.3, 0.5, 0.7]
# print(str(c1))

# nt11 = KzNucleotide(1,0,0,0)
# nt21 = KzNucleotide(0,1,0,0)
# nt31 = KzNucleotide(0,0,1,0)
# nt41 = KzNucleotide(0,0,0,1)
# nt51 = KzNucleotide(0,0.5,0,0.5)
# c11 = KzConsensus(strength=1, codonStart=3, sequence=[nt11, nt21, nt31, nt41,nt51, nt11, nt21, nt31, nt41,nt51, nt11]) #, factors=[0.1, 0.3, 0.5, 0.7]
# print("Seq:"+repr_sequence(c11.sequence))
# print("Led:"+repr_sequence(c11.leading()))
# print("Cod:"+repr_sequence(c11.codon()))
# print("TRL:"+repr_sequence(c11.trailing()))

c21 = new_KzConsensus((1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0,0.5,0.5))
print(str(c21))
print(c21.confidence_distribution("aaugucg"))
print(c21.confidence("aaugucg"))
print(c21.confidence_distribution("aaugucc"))
print(c21.confidence("aaugucc"))
print(c21.confidence_distribution("aaugugg"))
print(c21.confidence("aaugugg"))
print(c21.confidence_distribution("aauguga"))
print(c21.confidence("aauguga"))

c21 = new_KzConsensus((1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0,0,1))
print(str(c21))
print(c21.confidence_distribution("aaugucg"))
print(c21.confidence("aaugucg"))
print(c21.confidence_distribution("aaugucc"))
print(c21.confidence("aaugucc"))
print(c21.confidence_distribution("aaugugg"))
print(c21.confidence("aaugugg"))
print(c21.confidence_distribution("aauguga"))
print(c21.confidence("aauguga"))


c21 = new_KzConsensus((1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0.33,0.33,0.33))
print(str(c21))
print(c21.confidence_distribution("aaugucg"))
print(c21.confidence("aaugucg"))
print(c21.confidence_distribution("aaugucc"))
print(c21.confidence("aaugucc"))
print(c21.confidence_distribution("aaugugg"))
print(c21.confidence("aaugugg"))
print(c21.confidence_distribution("aauguga"))
print(c21.confidence("aauguga"))