
from initiator_set.kozak_calculator.kozak_calculator import *
from initiator_set.kozak_calculator.kozak_loader import *


def calculate_leaky(mrna: mRNA, *penalties: Callable[[int], float]):
    calculate_leaky_chronological(mrna, *penalties)
    # calculate_overlap(mrna)


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
    kozaks_of_ranked_weights: List[KzContext] = mrna.metadata['kozak_contexts']
    adjusted_weights: List[int] = mrna.metadata['adjusted_weights']

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

    mrna.metadata['leaking_of_chronological_weights'] = leaking_of_ranked_weights

    print()

# Calculate the sequences that overlap due to selection of start codon
def calculate_overlap(mrna: mRNA):
    # calculate_lengths(mrna)
    mrna.metadata['overlap_sequences'] = detect_overlap(mrna)


# # Calculate lengths of sequences in mrna
# # Result is in sequence_lengths_chronological
# # Is this the job for some other submodule?? put it here anyways
# def calculate_lengths(mrna: mRNA):
#     indices_aic: Dict[int, str] = mrna.metadata['indices_aic']
#     lengths: List[int] = []
#     for pos in indices_aic.items():
#         length = sequence_length(mrna, pos[0])
#         lengths.append(length)
#     mrna.metadata['sequence_lengths_chronological'] = indices_aic


# Scans an mrna for a stop codon, given the location of a start codon
def sequence_length(mrna: mRNA, start: int, stop_codons: tuple = ('UAG', 'UUA', 'UGA')) -> int:
    pos = 0
    for codon in Iterable(mrna, start, len(mrna.code)):
        pos = pos + 1
        if codon in stop_codons:
            return pos
    return -1


# Find missed stop codons from using other start codons
def detect_overlap(mrna: mRNA) -> List[Tuple[int, int]]:

    # Calculate ending positions
    result: List[Tuple[int, int]] = []
    ending_pos = []
    indices_aic: List[int] = mrna.metadata["locations_aic_chronological"]
    sequence_lengths: List[int] = mrna.metadata['sequence_lengths']
    for i in range(0, len(sequence_lengths)):
        start = indices_aic[i]
        length = sequence_lengths[i]
        ending_pos.append(start + length)
        pass

    # Calculate range overlaps
    for i in range(0, len(sequence_lengths)):
        for j in range(0, len(sequence_lengths)):
            if i != j:
                # i overlaps with j
                i_range = range(indices_aic[i], ending_pos[i])
                j_range = range(indices_aic[j], ending_pos[j])
                i_set = set(i_range)
                overlap = i_set.intersection(j_range)

                if len(overlap) > 0:
                    # rearrange such that first < second for consistency
                    first = indices_aic[i]
                    second = indices_aic[j]
                    if first >= second:
                        t = second
                        second = first
                        first = t
                    if (first, second) not in result:
                        result.append((first, second))

    return result


# Digital true/false value. Leaking occurs when the first start codon present is higher than a threshold value
# (default is 0.0).
def is_leaky(mrna: mRNA, threshold: float = 0.0) -> bool:
    return mrna.metadata['leaking_of_chronological_weights'][0] > threshold
