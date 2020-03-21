
from util.DataStructures import Tree
from typing import *

from fasta.IS_Fasta_Sequence import Sequence_Read
from map_aic.mapAIC import mapAICs
from kozak_calculator import kozak_calculator
from protein_targeting_and_localisation.protloc import tagLocStrings
from leaky_scan_detector import leaky_scan_detector
from gc_count.gc_count import getData

# Dependency tree of Initiator Set
# @formatter:off
module_flow: Tree = Tree(
# Fasta parsing
rep=Sequence_Read, children=[
    # Map AIC
    Tree(rep=mapAICs, children=[

        # Kozak calculator
        Tree(rep=kozak_calculator.calculate_kozaks, children=[
            # Leaky Scanning
            Tree(rep=leaky_scan_detector.calculate_leaky, children=[])
        ]),

        # Protein Localisation TODO needs implementation
        Tree(rep=tagLocStrings, children=[]),

        # GC Count
        Tree(rep=getData, children=[
            #TODO need IRES
                #TODO Needs uORFS
                    #TODO needs Ribosomal Assembly checker
        ])
    ])
])
# @formatter:on
#TODO perhaps a tree is not the best solution here because it closes in on annotation march
module_flow.children[0].potato = 1

print(module_flow)