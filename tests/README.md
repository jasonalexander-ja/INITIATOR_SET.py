# INITIATOR SET DEMO

In the adjoining folder you will find files to be used with INITIATOR SET to run a demonstration of its capabilities.

# Map AICs:

1. In Map AICs tab: Open FASTA File (top left of window) and select a FASTA file that contains a full genetic sequence to use, either in the form of CDNA, CDS or mRNA. We have a demo file for the BAG1 gene and another for just its CDS. If the whole gene FASTA file crashes the GUI, reload and try again with just the CDS, and report the issue in Gitlab.

2. Click the Data Selector to select the Sample Data Lee AICS Likelihoods Input.txt file. This will provide the codon weights for Map_AICs to use, based on Lee et al's paper from 2012. It is possible to manually enter and save a set of codon weights.

3. Temporary workaround for a stubborn bug: Untick and re-tick the 'Display on sequence' checkbox before you proceed further.

4. Click on Analyze. This will produce a multicoloured highlighting of the sequence in the top pane, based on the colours in the Codon Weights Data table.

NB: When we enable the Probability Waveform Display Mode, you can click it at this point to show the probabilities displayed in a pretty line graph representing the relative probabilities from 5` to 3` of the mRNA, of protein translation initiation.

NB: When we enable the Colour Selector, you will be able to choose colours to set for each of the codons in the table, to make it easier to pick out specific codons of interest.

# Kozak Calculator:

1. Use the Data Selector to select a correctly formatted Sample Kozaks text file - we have a few examples in the demo folder. Please note these are not production ready Sample Kozaks, we need to get more properly verified sources for that. These should be treated as files for demo perposes only. It is or will be possible to manually enter and save a set of Kozak contexts.

2. Click Analyze. The most likely to be used AICs' Kozak contexts are highlighted in red on the sequence, with the relative importance of each nucleotide represented by its font size, and with appropriate changes to the probability weighting in the middle pane.

NB: These changes will also be reflected in the Probability Waveform Display Mode when that is implemented.

NB: The Conserved Threshold and Conserved boxes require some further clarification in our documentation, for now in the demos please don't go into them.

# Leaky Scanning:

1. Click the Calculate button to see whether the sequence so far is likely to cause leaky scanning to be possible.

2. Click Translate to Protein to see each of the most likely AICs' protein sequences they would lead to.

NB: The Threshold box needs to be set to match real world leaky scanning thresholds, if they exist. This requires some further clarification in our documentation, for now in the demos please don't go into it.

# All other submodules:

All other submodules' tabs are as of 27th August 2022, only mockups of the GUI elements to act as a placeholder and guide to what functionality there will be.

### Author: Athamanatha Kitsune (atha@vulpinedesigns.com)
