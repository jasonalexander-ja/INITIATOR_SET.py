from initiator_set.util.mRNA import *
from initiator_set.kozak_calculator.kozak_loader import *
from initiator_set.map_aic_alternative.map_aic import *


# End user program

def calculate_kozaks(mrna: mRNA, kozaks: List[KzConsensus]):
    ranked_weights = mrna.metadata["ranked_weights"]
    if ranked_weights is None:
        raise ValueError("Map AIC not initialised")
    mrna.metadata["kozaks_of_ranked_weights"]: List[int] = []

    # Attach kozak strength to each ranked weight
    for start_index in ranked_weights:
        start_codon = deindexCodon(mrna.code[start_index])

        # Find Kozaks that surround the start_codon
        for kz in kozaks:
            if kz.codon().upper() != start_codon:
                continue

            leading_length = kz.codonStart
            context_start = start_index - leading_length
            context_end = context_start + len(kz.sequence)
            code = deindexRNA(mrna.code)

            # For now, skip kozaks that are too large to fix in mrna
            # This might be undesirable, but probably irrelevant considering:
            # 1. hard to read start codons too close to 5'
            # 2. start codons near 3' are probably useless as they have no information
            # to make it work though you would just have to pad z's around the context area
            if context_start < 0:
                continue
                # context_area = ("z" * abs(context_start)) + context_area
            if context_end > len(code):
                continue
                # context_area = context_area + ("z" * (context_end-len(mrna.code)))

            context_area = code[context_start:context_end].lower()
            similarity = kz.similarity(context_area)
            mrna.metadata["kozaks_of_ranked_weights"].append(similarity)
    pass
