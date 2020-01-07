from dataclasses import *
from typing import *

MAJORITY_MIN = 0.4 # Any KzNucleotide with a weight above this value will be part of the representation of the sequence
# CONSERVED_LIMIT = 75 # Any KzNucleotide with an influence above this value will be capitalised

# Represents an mRNA nucleotide, as part of a kozak consensus distribution.
@dataclass(frozen = True)
class KzNucleotide:
    # How important this nucleotide contributes to the kozak consensus, range 0 - 100
    # influence: float
    # All floats between 0 and 1 (inclusive, inclusive), representing distribution
    # They must all add up to 1 as they basically represent percentages
    a: float
    u: float
    g: float
    c: float

    verify: bool = False
    def valid(self) -> bool:
        return self.a + self.u + self.g + self.c == 1
    #def important(self) -> bool:
    #    return self.influence >= CONSERVED_LIMIT
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
        result=[tmp[0]] # index at 0 will be largest
        # Get other nucleotides with equal distribution
        for i in range(1, len(tmp)):
            t = tmp[i]
            if t[1] >= majority_min or t[1] == tmp[0][1]:
                result.append(t)
            else: break
        return result

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
        result = "("
        for i in nucleotides:
            result += i + "|"
        result = result[:-1]+")"
        return result

def repr_sequence(nucleotides : List[KzNucleotide]) -> str:
    result = ""
    for i in nucleotides:
        result += str(i)
    return  result


@dataclass
class KzConsensus:
    strength: float
    codonStart: int
    sequence : List

    codonLength: int = 3
    verify: bool = False
    def __post_init__(self):
        if not self.verify: pass
        #TODO verify data here, if needed


print(KzNucleotide(.5,.5,0,0).__str__())
print(KzNucleotide(1,0,0,0).__str__())
print(KzNucleotide(1,0,0,0).__str__())
print(KzNucleotide(1,0,0,0).__str__())
print(KzNucleotide(0,0,1,1).__str__())
print(KzNucleotide(.5,0,0.5,0).__str__())
print(KzNucleotide(.25,.25,.25,.25).__str__())
print(KzNucleotide(.25,.25,.25,.25).__str__())
print(KzNucleotide(.33,.25,.25,.18).__str__())
print(KzNucleotide(.18,.25,.25,.33).__str__())
print(KzNucleotide(.25,.251,.25,.249).__str__())
print(KzNucleotide(.5,0,0.5,0).__str__())
#x: KzConsensus = KzConsensus(1.0, 1, None)
#print(x.__str__())