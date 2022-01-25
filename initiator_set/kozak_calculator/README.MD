# Kozak Calculator

The purpose of this submodule is to calculate the possible Kozak Contexts of a given mrna strand.

Inputs: 
- mRNA strand, initialised with Map AIC
- list of relevant kozak consensuses

Outputs:
- Analogue similarity distribution mrna sequence
- Analogue similarity ratio to an mrna sequence
- Digital true or false value backed by a single minimum threshold value (self defined)

Features:
- Start codon agnostic (not specific to AUG)
- Textual parser to make it easier to deal with lots of different kozak consensus sequences
- Each position in a KzConsensus definition has weight that affects how much signals are modified
- Analogue outputs make it easier to define thresholding mechanics

Description of files:
- kozak_consensus.py - stores important classes and model code for kozak calculation
- kozak_loader.py - loads kozak consensus sequence definitions from file
- kozak_calculator.py - calculates the kozaks of all initiator codons in an mrna where Map AIC was initialised

> As of # ccff10d, this is currently a 'feature-complete island', waiting for bugs to be fixed on the original map_aic.

### Author: Akasha Peppermint (tehrandommagik@gmail.com)
