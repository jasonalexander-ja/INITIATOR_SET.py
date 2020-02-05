import itertools
from dataclasses import dataclass
from typing import *
from initiator_set.util.mRNA import *


def map_aic(mrna: mRNA, weights: Dict[str, float]):
    mrna.metadata["baseWeights"]: List = []

    # Attach weights for each codon
    for indexedCodon in mrna.code:
        codon = deindexCodon(indexedCodon)
        weight_entry = weights.get(codon)
        value = 0.0 if weight_entry is None else weight_entry
        mrna.metadata["baseWeights"].append(value)

    # Attach the locations for each AIC in different views

    # Dictionary of initiator codons by locations in the mrna, indexed like so:
    # key = codon, val = List of locations of codon in mrna
    mrna.metadata["locations_aic"]: Dict[str, List[int]] = {}
    for codon in weights.keys():
        mrna.metadata["locations_aic"][codon] = []
    for i in range(0, len(mrna.code)):
        indexed_codon = mrna.code[i]
        codon = deindexCodon(indexed_codon)
        weight_entry = weights.get(codon)
        if weight_entry is None:
            continue
        mrna.metadata["locations_aic"][codon].append(i)

    # Dictionary of index positions of where starting initiator codons are located,
    # indexed like so:
    # key = location in codon, value = codon

    # This is basically a dupe of locations_aic in memory but is useful to decrease computational load
    # Because inevitably some dependent module is going to need both:
    # - the locations of all of specific initiator codons
    # - flat list of all locations of potential initiator codons
    # So we may as well calculate it now while we are here
    mrna.metadata["indices_aic"]: Dict[int, str] = {}
    for i in range(0, len(mrna.code)):
        indexed_codon = mrna.code[i]
        codon = deindexCodon(indexed_codon)
        weight_entry = weights.get(codon)
        if weight_entry is None:
            continue
        mrna.metadata["indices_aic"][i] = codon


    # Rank the AIC locations by AIC weight

    sorted_aics: List = list(sorted(weights.items(), key=lambda x: x[1], reverse=True))  # [Tuple[str, float]]
    mrna.metadata["ranked_weights"]: List[int] = []
    for i in range(0, len(sorted_aics)):
        aic = sorted_aics[i]
        locations = mrna.metadata["locations_aic"].get(aic[0])
        if locations is None:
            continue
        for loc in locations:
            mrna.metadata["ranked_weights"].append(loc)

    mrna.metadata["weights_dict"] = weights

    # Calculate adjusted weights
    # I saw this entry was lying around in the original map AIC but not calculated
    # I'm taking it as normalising the weights so that all values are between 0 and 1
    # Where 1.0 was whatever the maximum weighted entry previously was
    # Probably not even needed

    # Find max weight
    w_max = 0
    for i in weights.values():
        if i > w_max:
            w_max = i

    # Convert it to a tuple
    adjusted_weights = {}
    for i in weights.items():
        adjusted_weights[i[0]] = i[1] / w_max
    mrna.metadata['adjusted_weights'] = adjusted_weights




