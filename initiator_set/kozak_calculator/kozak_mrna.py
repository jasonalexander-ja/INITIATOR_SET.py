########################################################################################################################
# Ties kozak calculator into INITIATOR SET
########################################################################################################################

from initiator_set.kozak_calculator.kozak_calculator import *
from initiator_set.util.mRNA import *


# Calculates the similarity distribution of an mrna's kozak to a given kozak consensus sequence
# Output is stored in mrna metadata
def kozak_strength_distribution(mrna: mRNA, kozak: KzConsensus):
    mrna.metadata["kozak_strength_distribution"] = kozak.similarity_distribution(mrna_extract_kozak(mrna))


# Calculates the similarity of an mrna's kozak to a given kozak consensus sequence
# Output is stored in mrna metadata as a float value representing strength value
def kozak_strength(mrna: mRNA, kozak: KzConsensus):
    mrna.metadata["kozak_strength"] = kozak.similarity(mrna_extract_kozak(mrna))


# In order to get a result, the area of the kozak needs to be known (for right now)
def mrna_extract_kozak(mrna: mRNA) -> str:
    startpos: int = mrna.metadata.get("kozak_start")
    endpos: int = mrna.metadata.get("kozak_end")
    kozak_str = mrna.code[startpos::endpos]
    return kozak_str

