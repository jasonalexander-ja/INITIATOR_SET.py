from kozak_calculator.kozak_calculator import *
from kozak_calculator.kozak_loader import *
from util.mRNA import *


def calculate_leaky(mrna: mRNA, *penalties: Callable[[int], float]):
    calculate_leaky_chronological(mrna, *penalties)
    calculate_lengths(mrna)


# Given an mRNA, calculate the leakiness based off the strength of the kozaks and the weight of the start codons.
# Requires Kozak Calculator to be initialised
# Result is an entry in mrna.metadata, as an array of floats between 0.0 and 1.0 representing leakiness level
# Where 0.0 means highest weight start codon with perfect kozak and no penalty scorings
# And higher values mean less start codon weight/kozak strength/higher penalty scorings
#
# penalties: a lamda function. Result is blended evenly into the final leakiness result.
# arguments for lambda are distance to 5' cap, return is penalty factor between 0.0 and 1.0
#
# This version of the function goes off of the ordering of the start codons as they appear naturally in mrna sequence
def calculate_leaky_chronological(mrna: mRNA, *penalties: Callable[[int], float]):
    if not mrna.Metadata.get("kozakContexts"):
        raise ValueError("Kozak Contexts have not been calculated yet")
    kozaks_of_ranked_weights: List[KzContext] = mrna.Metadata.get("kozakContexts")
    adjusted_weights: List[int] = mrna.Metadata.get('adjustedWeights')

    leaking_of_ranked_weights: List[float] = []
    for i in range(0, len(kozaks_of_ranked_weights)):
        context = kozaks_of_ranked_weights[i]
        pos = context.initiator_start
        kozak = kozaks_of_ranked_weights[i].strength
        rel_weight = adjusted_weights[i]

        combined_penalties = 0
        for j in penalties:
            combined_penalties += j(pos)

        # TODO need to apply some sort of weight mechanic for each of these factors
        # because right now having a strong kozak means as much as a good start codon,
        # and combined penalties also means just as much
        # but for now the mean average for codon weight, kozak strength, and combined_penalties should suffice
        leaking_factor = 1 - (rel_weight + kozak + combined_penalties) / (2.0 + len(penalties))

        leaking_of_ranked_weights.append(leaking_factor)

    mrna.Metadata['leaking_of_chronological_weights'] = leaking_of_ranked_weights

    print()


# Calculate lengths of sequences in mrna
# Result is in sequence_lengths
# Is this the job for some other submodule?? put it here anyways i need it
def calculate_lengths(mrna: mRNA):
    lengths: List[int] = []
    for x in range(0, len(mrna.Code)):
        lengths.append(sequence_length(mrna, x))
    mrna.Metadata['sequence_lengths'] = lengths


# Scans an mrna for a stop codon, given the location of a start codon
def sequence_length(mrna: mRNA, start: int, stop_codons: tuple = ('UAG', 'UUA', 'UGA')) -> int:
    le = 0
    for i in range(start, len(mrna.Code), 3):
        codon = deindexCodon(mrna.Code[i])
        le += 1
        if codon in stop_codons:
            break
    return le


# Determines whether sequences overlap, starting at position (as first character of starting codon)
def is_overlap(mrna: mRNA, one: int, two: int) -> bool:
    if mrna.Metadata['sequence_lengths'] is None:
        calculate_lengths(mrna)
    x = one if (one < two) else two
    y = two if (one < two) else one
    return mrna.Metadata['sequence_lengths'][x] + x > + y

# Digital true/false value. Leaking occurs when the first start codon present is higher than a threshold value
# (default is 0.0).
def is_leaky(mrna: mRNA, threshold: float = 0.0) -> bool:
    return mrna.Metadata['leaking_of_chronological_weights'][0] > threshold
