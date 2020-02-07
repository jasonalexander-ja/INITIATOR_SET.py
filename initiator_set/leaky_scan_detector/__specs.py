# Process Map AIC


# Process kozaks


# Process leaky scanning
# Input list of weights, indexed by aic location, valued by kozak weight ratio
from typing import *

from initiator_set.util import mRNA
import operator

from initiator_set.util.mRNA import deindexCodon, deindexRNA


# def process(mrna: mRNA):
#     kozakness: List[float] = mrna.metadata['kozaks_of_ranked_weights']
#     locations_aic: Dict[str, float] = mrna.metadata['locations_aic']

# TODO need to define some sort of threshold mechanism,
#  since it's likely that some initiator codons are near-equal weight
def is_weak(mrna: mRNA, ranked_weight_index: int) -> bool:
    strand = deindexRNA(mrna.code)
    rw_entry = mrna.metadata['ranked_weights'][ranked_weight_index]
    codon = strand[rw_entry:rw_entry+3]

    # if the kozak is weak then regardless of what happen it is weak
    # if (mrna.metadata['kozaks_by_ranked_weight'][ranked_weight_index] < )
    # weight = mrna.metadata['weights_dict']
    # but if the kozak is strong, and the codon is strong, then it's not weak
    pass


def process2(kozakness: List[float], locations_aic: Dict[str, float]):
    # kozakness: [0.4 1.0 0.5 0.1]
    # locations: [{'AUG': [6, 15, 38, 45]}]

    # Output:
    # yes no kinda kinda
    # don't i just calculate the kozak likelihood of all aics? sounds really simple
    # No because remember stuff to close to 5' get a penalty
    # So create a penalty function, probably an external function

    # then answer:
    # True or false - there are no leaky scanning mechanisms involved in this RNA (min threshold param default of 0)
    # Given a minimum threshold (default value of 0), how many starting positions are there?
    # Highest likelihood to the first initiator codon with a kozak threshold higher than 'x'
    # Distance to max value

    # There are other desired methods such as
    # What is the likelihood at 'x'? - this may not be useful due to mutations, particularly,
    #  insertion and deletion mutations affecting ordering, or mutations in the start codon itself destroying it
    # I could just populate the kozakness list of floats into the mrna metadata here,
    #  after all it is tightly bound to kozak submodule

    pass
