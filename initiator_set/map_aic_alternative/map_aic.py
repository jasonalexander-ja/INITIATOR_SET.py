from dataclasses import dataclass
from typing import *
from initiator_set.util.mRNA import *
from itertools import *

# Magic method that spits out all codons in a list, a codon being a sequence of 3 nucleotides
codons: List[str] = list(map(''.join, product(["A", "U", "G", "C"], ["A", "U", "G", "C"], ["A", "U", "G", "C"])))


# Struct for storing codon and weight
@dataclass
class AICWeights:
    codon: str
    weight: float


# Collection of possible AICs
# Duplicate codons are replaced
@dataclass
class AICDictionary:
    # codon, weight
    aic_dict: Dict[str, float]

    def __init__(self, aic_weights):
        self.aic_dict = {}
        if len(aic_weights) > 0:
            if type(aic_weights[0]) is tuple:
                for i in aic_weights:
                    self.aic_dict[i[0]] = i[1]
            elif type(aic_weights[0]) is AICWeights:
                for i in aic_weights:
                    self.aic_dict[i.codon] = i.weight

    # Sorted codon strings by highest weight in dictionary
    def sorted_by_weights(self) -> List[str]:
        return sorted(self.aic_dict.items(), key=lambda x: x[1])


# Collection of locations of candidate AICs along an mrna strand
@dataclass
class AICMap:
    # codon, location in strand
    aics: Dict[str, List[int]]

    # collapses the dictionary into a sorted list, where positions closer to 0 are higher priority codons
    # argument can be either AICDictionary or resulting call of sorted_by_weights,
    # which is a list of strings sorted by priority in descending order
    def collapse_by_priority(self, codons_by_str_priority_or_aic_dictionary) -> List[Tuple]:
        result = []
        c = codons_by_str_priority_or_aic_dictionary
        codons_by_priority = c.sorted_by_weights() if c is AICDictionary else c
        for e in codons_by_priority:
            ex = self.aics.get(e)
            if ex is None:
                self.aics[e] = []
            result.extend(self.aics.get(e))
        return result

    # collapses the dictionary into a sorted list, where elements closer to 0 are closer to 5' of mRNA strand
    def collapse_by_position(self) -> List:
        result = []
        for elem in sorted(self.aics.items(), key=lambda x: x[1]):
            result.extend((elem[0], elem[1]))
        return result


def map_aic(aic_dictionary: AICDictionary, sequence: str) -> AICMap:
    # aic_weights = aic_dictionary.sorted_by_weights()
    aics: Dict[str, List[int]] = {}

    # Search every trio of nucleotides as the start of codon transcription is not established
    for i in range(0, len(sequence)-2, 1):  # it's 1 not 3
        trio: str = sequence[i:i+3]
        if trio in aic_dictionary.aic_dict.keys():
            entry = aics.get(trio)
            if entry is None:
                aics[trio] = []
            aics[trio].append(i)

    return AICMap(aics)
