# Title: IS_Main.py
# Description: Initiator Set main script file
#
# Author: Jordan Eckhoff
# e-mail: jeckhoff@vulpinedesigns.com
#
# Contributors: N/A
# Contributor e-mails: N/A
#
# Creation Date:  10 Jul 2018
# Latest Version: 11 Jul 2018
#
# Usage Instructions: When prompted, open a .fa FASTA file. This file will ???

import IS_Sequence # Custom module for working with FASTA files

from tkinter import Tk                         #
from tkinter.filedialog import askopenfilename # Asks user to select a .fa FASTA file
Tk().withdraw()                                #

FastaPath = askopenfilename() # Stores file's PATH ## combine with with statement below?

with open(FastaPath,'r') as FastaFile: # Opens the selected .fa file via its PATH
    Sequences = IS_Sequence.FASTA_Seq(FastaFile.readlines()) # Creates a list of custom FASTA_Seq objects, each of which contains a single sequence from the FASTA file and its associated metadata as seperate properties, Seq and Meta respectively

print(Sequences.Meta)
print(Sequences.Seq)
