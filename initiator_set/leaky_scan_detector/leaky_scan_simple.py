from initiator_set.util import mRNA
from initiator_set.util.mRNA import deindexRNA

# There is limited knowledge on how leaky scanning works
# But the basic way it works is that weak starting positions may be skipped by a ribosome
# and start at a later position

# A weak starting position can be
# But to code this in requires a knowledge of what counts as weak and strong
# That needs to be implemented in kozak_calculator before able to be implemented

# Supposedly leaky scanning also relates to the ability of a ribosome to detect stop codons,
# e.g: due to insertion/deletion mutations in the transcription sequence altering the entire frameline,
# or the stop codon itself getting mutated, or a faulty ribosome
# but that's not implemented yet


# Simple 'i've done something' method that matches weak initator then strong initiator
# Requires only Map AIC to be initialised
def is_leaky(mrna: mRNA) -> bool:
    strand = deindexRNA(mrna.code)
    ranked_weights = mrna.metadata['ranked_weights']
    for i in sorted(ranked_weights):
        codon = strand[i:i+3]
        rel_weight = mrna.metadata['adjusted_weights'][codon]
        if rel_weight <= 0:
            continue
        else:
            return rel_weight < 1.0
    # TODO needs to account for strong initiator in weak kozak context followed by strong initiator
