########################################################################################################################
#
# Given a comparison nucleotide sequence and a starting position,
# this calculator will compare the similarity score,
# with respect to possible alternations to the kozak in real mRNA
#
# For example, the currently known optimal kozak for mammalian mRNA is 'gccgccaccAUGg'
# However, the most important bits are the second A (which can also be a G), and the last G.
# The other bits do not matter as much but do help.
# (see wikipedia and vulpine designs wiki for more information)
#
# This is an analogue calculator, the output is not true or false but in signals.
# You can define a threshold mechanism of your choice to determine what counts as 'aligns to kozak'
# e.g with sample_kozaks.txt you could simply define 0.5 as a strong-align minimum and that allows the...
# example above to pass with second G and last G matched, even with every other context bit mismatched.
#
# Different Kozak Consensus Sequences can be represented as different KzConsensus instances.
# Each Kozak Consensus Sequence can have any initiator codon, not just AUG/Methionine.
# Due to the difficulty of instantiating KzConsensus instances, and because
# there are entirely different Kozak Consensus Sequences and weights for different species, most still unstudied,
# it is recommended to store them in files and construct them using methods in the kozak_loader.py file
#
########################################################################################################################

from dataclasses import *
from typing import *

MAJORITY_MIN = 0.4  # Any KzNucleotide with a weight above this value will be part of the representation of the sequence


########################################################################################################################
#
# Represents a nucleotide position, as part of a kozak consensus distribution for mRNA,
# as weighted values of possible nucleotides
#
########################################################################################################################
@dataclass
class KzNucleotide:
    # All floats between 0 and 1 (inclusive, inclusive), representing distribution
    # They should add up as close to 1 as possible as they are supposed represent percentages
    a: float
    u: float
    g: float
    c: float

    # Positions of high importance are conserved. Either positive, or -1 if part of the initiation codon
    importance: int

    def tuples(self) -> List[Tuple[str, float]]:
        return [('a', self.a), ('u', self.u), ('g', self.g), ('c', self.c)]

    def dict(self) -> Dict[str, float]:
        return {'a': self.a, 'u': self.u, 'g': self.g, 'c': self.c}

    # Returns the nucleotides ordered by maximum weight as a list of tuples
    def sorted(self) -> List[Tuple[str, float]]:
        result: List[Tuple[str, float]] = self.tuples()
        result.sort(key=lambda t: t[1], reverse=True)
        return result

    # Returns the nucleotides with the maximum distributions
    def maximums(self) -> List[Tuple[str, float]]:
        tmp: List[Tuple[str, float]] = self.sorted()
        result = [tmp[0]]  # index at 0 will be largest
        # Get other nucleotides with equal distribution
        for i in tmp:
            if i[1] == tmp[0][1]:
                result.append(i)
            else:
                break
        return result

    # Returns the nucleotides with distributions above dominant level
    def dominants(self, majority_min: float = MAJORITY_MIN) -> List[Tuple[str, float]]:
        tmp: List[Tuple[str, float]] = self.sorted()
        largest: Tuple[str, float] = tmp[0]
        result: List[Tuple[str, float]] = []  # index at 0 will be largest
        # Get other nucleotides with equal distribution
        for t in tmp:
            if t[1] >= majority_min or t[1] == largest[1]:
                result.append(t)
            else:
                break
        return result

    # nucleotide_char is one of 'a', 'u', 'g', or 'c'
    def weight_of(self, nucleotide_char: str) -> float:
        return self.dict().get(nucleotide_char.lower(), 0)

    # I do not think this function is right
    def is_conserved(self):
        # return self.dominants()[0][1] > 0.25
        return self.importance > 6

    # Returns:
    # If single dominant, returns the nucleotide by itself
    # If multiple dominants, returns the nucleotides surrounded by (), split by |
    def __str__(self):
        nucleotides: str = ""
        tmp: List[Tuple] = self.dominants()
        for i in tmp:
            nucleotides += i[0]
            pass
        if len(nucleotides) <= 1: return nucleotides
        result = "["
        for i in nucleotides:
            result += i + "|"
        result = result[:-1] + "]"
        return result


########################################################################################################################
#
# Represents a Kozak Consensus Sequence, as a distribution of possible nucleotides in each position of the sequence
#
########################################################################################################################
@dataclass
class KzConsensus:
    codonStart: int
    sequence: List[KzNucleotide]

    codonLength: int = 3  # this should always be 3 anyway...

    def leading(self) -> List[KzNucleotide]:
        return self.sequence[0: self.codonStart]

    # Because the codon of a Kozak is certain, this just returns a string
    def codon(self) -> str:
        result = ""
        codon = self.sequence[self.codonStart: self.codonStart + self.codonLength]
        for e in codon:
            result += e.dominants()[0][0]
        return result

    def trailing(self) -> List[KzNucleotide]:
        return self.sequence[self.codonStart + self.codonLength: len(self.sequence)]

    def total_weight(self):
        return sum(i.maximums()[0][1] * i.importance for i in self.sequence) + self.codonLength * 2
        # * 2 because special weight of -1

    # Given a comparison sequence, calculates the distribution of confidence
    # returned values are a list of floats, indexed to comparison_sequence, corresponding to
    # the similarity of the comparison sequence to self.sequence.
    # Comparison_sequence must contain initiation codon.
    # If it is missing, there will be negative 1s in the distribution
    def similarity_distribution(self, comparison_sequence: str, comparison_start: int = 0) -> List[float]:
        comparison_length = (len(comparison_sequence) - comparison_start)
        result: List[float] = [0.0] * comparison_length

        for i in range(0, min(comparison_length, len(self.sequence))):
            a_kz_nucleotide = self.sequence[i]
            b_str = comparison_sequence[i + comparison_start]

            weight = a_kz_nucleotide.weight_of(b_str)
            importance = a_kz_nucleotide.importance

            confidence = weight * importance if (importance >= 0) else 1

            # Malformed input check
            if importance < 0 and b_str not in str(a_kz_nucleotide):
                confidence = -1

            result[i] = confidence
        return result

    # Sum of similarity_distribution; a convenience method
    def similarity_tally(self, comparison_sequence: str, comparison_start: int = 0) -> int:
        return sum(self.similarity_distribution(comparison_sequence, comparison_start))

    # Given a comparison sequence, calculates the similarity,
    # or how 'strong' the comparison sequence aligns with this consensus.
    # Returned value is between 0 and 1.
    # Will return 0 in the case where the initiator codon is not present.
    # You should prevent this from happening if possible as it should be given
    # (according to the problem statement I was given)
    def similarity(self, comparison_sequence: str, comparison_start: int = 0, codon_length: int = 3) -> float:
        c_dist: List[float] = self.similarity_distribution(comparison_sequence, comparison_start)
        if -1 in c_dist:
            return 0
        return (sum(c_dist) - codon_length) / self.total_weight()

    def __repr__(self):
        return self.__str__()

    # The structure of the representation of the consensus is as follows:
    # () = part of sequence that has no siginificant impact on the consensus
    # (i.e: just padding)
    # [] = part of the sequence that has multiple majority candidates, split by |
    # (e.g: accAUGG and gccAUGG are both candidate sequences/subsequences)
    def __str__(self) -> str:
        result = ""
        representeds: List[str] = []
        for i in self.sequence:
            representeds.append(str(i))
        for nucleotide, kz_nucleotide in zip(representeds, self.sequence):
            result += nucleotide.upper() if kz_nucleotide.is_conserved() else nucleotide
        return result


# Convenience builder for KzConsensus constructor using simplified parameters. Meant for debugging,
# because even with this it is still very hard to instantiate KzConsensus objects and populate them with meaningful data
def new_KzConsensus(*anynomous_weights_objects: Iterable[object]):
    o = anynomous_weights_objects
    sq: List[KzNucleotide] = []
    if o is Dict:
        for i in o:
            sq.append(KzNucleotide(i.a, i.u, i.g, i.c, importance=1))
    if type(o) in [list, tuple]:
        for i in o:
            sq.append(KzNucleotide(i[0], i[1], i[2], i[3], importance=1))
    else:
        raise ValueError
    return KzConsensus(sequence=sq, codonStart=0)


def repr_sequence(nucleotides: List[KzNucleotide]) -> str:
    result = ""
    for i in nucleotides:
        result += str(i)
    return result
