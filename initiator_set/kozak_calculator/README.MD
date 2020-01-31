# Kozak Calculator

The purpose of this submodule is to calculate the possible Kozak Contexts of a given mrna strand.

Inputs: 
- mRNA strand, initialised with Map AIC
- list of relevant kozak consensuses

Outputs:
- Analogue similarity distribution mrna sequence
- Analogue similarity ratio to an mrna sequence
- Digital true or false value backed by a single minimum threshold value (self defined)

kz_calculator_runner.py is an end user program for INITIATOR SET, 
for now it just attaches similarity ratio to any initiator codon defined by Map AIC

> As of # ccff10d, this is currently a feature-complete island, waiting for bugs to be fixed on other submodules.

### Author: Akasha Peppermint (tehrandommagik@gmail.com)
