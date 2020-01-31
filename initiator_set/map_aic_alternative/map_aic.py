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

    # Attach the locations for each AIC
    mrna.metadata["locations_aic"] = {}
    for codon in weights.keys():
        mrna.metadata["locations_aic"][codon] = []
    for i in range(0, len(mrna.code)):
        indexed_codon = mrna.code[i]
        codon = deindexCodon(indexed_codon)
        weight_entry = weights.get(codon)
        if weight_entry is None:
            continue
        mrna.metadata["locations_aic"][codon].append(i)

    sorted_aics: List[Tuple[str, float]] = list(sorted(weights.items(), key=lambda x: x[1], reverse=True))
    # Rank the AIC locations by AIC weight
    mrna.metadata["ranked_weights"]: List[int] = []
    for i in range(0, len(sorted_aics)):
        aic = sorted_aics[i]
        locations = mrna.metadata["locations_aic"].get(aic[0])
        if locations is None:
            continue
        for loc in locations:
            mrna.metadata["ranked_weights"].append(loc)


