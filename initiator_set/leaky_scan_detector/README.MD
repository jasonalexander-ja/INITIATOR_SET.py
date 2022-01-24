# Leaky Scan Detector

The purpose of this submodule is to detect leaking of start codons. Leaky scanning occurs when a 
start codon with suboptimal weight or kozak strength is sometimes skipped over by scanning ribosomes.

Note that this submodule does NOT take in ribosome capability and health factors into account.
Only factors in dealing with the position and context of start codons in the mRNA strand. 

The detector spits out a normalised mean distribution between
 start codon weight, kozak factor, and each of the penalty scoring mechanisms.
 
This may be undesirable as the weights of the start codons could mean more than the kozak
for example, but we don't know what those modifiers are, so for now this will have to do.
The scoring system can be changed later.

Some additional research is needed to improve on the functionality of this module.
(read: 'Protein 'intentionally' terminates own synthesis by destabilizing synthesis machinery').


It was suggested that leakage of STOP codons due to selection of start codon be implemented,



Inputs: 
- mRNA strand, initialised with Map AIC and Kozak Calculator
- Optional penalty scoring mechanics, meant for things like ribosome start codon
 misdetection when distance to 5' cap is too close
(this is externalised because we don't know exactly what they are yet, aside from the data
Marilyn Kozak published in one of their papers, I can't remember which paper I read it from)

Outputs:
- Analogue output:
leaking_of_chronological_weights and leaking_of_ranked_weights, which are Lists that contain 
float values between 0.0 and 1.0 indicating likelihood of leakage

- Digital output:
    - True/false Whether there is an instance where a weak initiation context is followed by
    a strong initiation context, leading to potential leakage past the weak one

Features:
- Takes in all features of kozak calculator and map aic into account

Description of files:
- leaky_scan_detector.py - main file, call methods from it.

### Author: Akasha Peppermint (tehrandommagik@gmail.com)
