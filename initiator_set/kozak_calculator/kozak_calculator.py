########################################################################################################################
#
# Methods to deal with tieing this submodule into Initiator Set.
# Works in conjunction with Map AIC to determine kozaks of all initiator codons determined by Map AIC.
#
########################################################################################################################
from dataclasses import dataclass
from kozak_calculator.kozak_consensus import KzConsensus
from kozak_calculator.kozak_loader import interpret_kozak_file
from util.mRNA import mRNA, deindexCodon, deindexRNA
from typing import *


@dataclass
class KzContext:
    context_start: int
    context_end: int
    initiator_start: int
    strength: float
    consensus: KzConsensus

    def __repr__(self):
        return "{}..{}={} ({})".format(str(self.context_start), str(self.context_end), str(self.strength), str(self.consensus))


# Given an mrna strand, calculate all the kozaks.
# Result is stored in mrna's metadata dictionary as
# kozaks_of_ranked_weights
# This is the kozak strength ratio of all initiator codon positions indexed by their corresponding elements
# in ranked_weights
#
# Map AIC needs to be initialised before this method is called
# kozaks_or_kozak_file can be either result of a call to kozak_loader.interpret_kozak_file(), or
def calculate_kozaks(mrna: mRNA, kozaks_or_kozak_file: Union[List[KzConsensus], str]):
    if type(kozaks_or_kozak_file) is list:
        kozaks = kozaks_or_kozak_file
    elif type(kozaks_or_kozak_file) is str:
        with open(kozaks_or_kozak_file) as kz_raw:
            kozaks = interpret_kozak_file(kz_raw, kozaks_or_kozak_file)

    kozak_start_codons = []
    for i in kozaks:
        kozak_start_codons.append(i.codon())

    kozaks_of_chronological_weights: List[float] = []
    kozak_contexts: List[KzContext] = []

    # Attach kozak strength to each codon in mrna.code
    for start_index in range(len(mrna.code)-2):
        start_codon = deindexCodon(mrna.code[start_index])

        try:
            kz_i = kozak_start_codons.index(start_codon.lower())
            kz = kozaks[kz_i]

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
            kozaks_of_chronological_weights.append(similarity)

            kozak_context = KzContext(context_start=context_start, context_end=context_end, initiator_start=start_index,
                                      strength=similarity, consensus=kz)
            kozak_contexts.append(kozak_context)

        except ValueError:
            kozaks_of_chronological_weights.append(0)

    mrna.metadata["kozak_contexts"] = kozak_contexts
    mrna.metadata["kozaks_of_starts"] = kozaks_of_chronological_weights
