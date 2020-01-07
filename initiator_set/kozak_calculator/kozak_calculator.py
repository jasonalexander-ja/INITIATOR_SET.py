from dataclasses import *
from typing import *

MAJORITY_MIN = 0.4 # Any KzNucleotide with a weight above this value will be part of the representation of the sequence

# Represents an mRNA nucleotide, as part of a kozak consensus distribution.
@dataclass(frozen = True)
class KzNucleotide:
    # All floats between 0 and 1 (inclusive, inclusive), representing distribution
    # They must all add up to 1 as they basically represent percentages
    a: float
    u: float
    g: float
    c: float

    verify: bool = False
    def valid(self) -> bool:
        return self.a + self.u + self.g + self.c == 1
    def tuples(self) -> List[Tuple[str, float]]:
        return [('a', self.a),('u', self.u),('g', self.g),('c', self.c)]
    def dict(self) -> Dict[str, float]:
        return {'a': self.a,'u': self.u,'g': self.g,'c': self.c}

    # Returns the nucleotides ordered by maximum weight as a list of tuples
    def sorted(self) -> List[Tuple[str, float]]:
        result: List[Tuple[str, float]] = self.tuples()
        result.sort(key=lambda t:t[1], reverse=True)
        return result

    # Returns the nucleotides with the maximum distributions
    def maximums(self) -> List[Tuple[str, float]]:
        tmp: List[Tuple[str, float]] = self.sorted()
        result=[tmp[0]] # index at 0 will be largest
        # Get other nucleotides with equal distribution
        for i in tmp:
            if i[1] == tmp[0][1]:
                result.append(i)
            else: break
        return result

    # Returns the nucleotides with distributions above dominant level
    def dominants(self, majority_min = MAJORITY_MIN) -> List[Tuple[str, float]]:
        tmp: List[Tuple[str, float]] = self.sorted()
        largest: Tuple[str, float] = tmp[0]
        result: List[Tuple[str, float]] = [] # index at 0 will be largest
        # Get other nucleotides with equal distribution
        for t in tmp:
            if t[1] >= majority_min or t[1] == largest[1]:
                result.append(t)
            else: break
        return result

    def is_conserved(self):
        return self.dominants()[0][1] > 0.25

    def __post_init__(self):
        if not self.verify: pass
        #TODO verify data here, if needed

    # Returns:
    # If single dominant, returns the nucleotide by itself
    # If multiple dominants, returns the nucleotides surrounded by (), split by |
    def __str__(self):
        nucleotides : str = ""
        tmp : List[Tuple] = self.dominants()
        for i in tmp:
            nucleotides += i[0]
            pass
        if len(nucleotides) <= 1: return nucleotides
        result = "["
        for i in nucleotides:
            result += i + "|"
        result = result[:-1]+"]"
        return result

def repr_sequence(nucleotides : List[KzNucleotide]) -> str:
    result = ""
    for i in nucleotides:
        result += str(i)
    return result


@dataclass
class KzConsensus:
    strength: float
    codonStart: int
    sequence : List[KzNucleotide]

    codonLength: int = 3
    verify: bool = False
    def __post_init__(self):
        if not self.verify: pass
        # if len(self.factors) == 0:
        #     setattr(self, 'factors', [CONSERVED_LIMIT] * len(self.sequence))
        #TODO verify data here, if needed
        # if len(sequence) != len(factors) raise ValueError()

    def leading(self):
        return self.sequence[0 : self.codonStart]

    def codon(self):
        return self.sequence[self.codonStart : self.codonStart + self.codonLength]

    def trailing(self):
        return self.sequence[self.codonStart + self.codonLength: len(self.sequence)]

    # The structure of the representation of the consensus is as follows:
    # () = part of sequence that has no siginificant impact on the consensus
    # (i.e: just padding)
    # [] = part of the sequence that has multiple majority candidates, split by |
    # (e.g: accAUGG and gccAUGG are both candidate sequences/subsequences)
    def __str__(self) -> str:
        result = ""
        representeds : List[str] = []
        for i in self.sequence:
            representeds.append(str(i))
        for nucleotide, kz_nucleotide in zip(representeds, self.sequence):
            result += nucleotide.upper() if kz_nucleotide.is_conserved() else nucleotide
        return result
    # TODO I am not sure what counts as a 'dominant' gene in gene expression
    # e.g whether a gene that has 0.1% more distribution than others should count as part of the expression
    # right now I have it set up so that it simplifies the expression when ^ is so
    # This probably only matters for representing bases that vary a lot in the sequence, as I don't really know at what point
    # bases are truncated off the representation, or if it's just an arbitrary point

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