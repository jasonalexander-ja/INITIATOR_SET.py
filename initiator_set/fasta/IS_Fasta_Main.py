# Title: IS_Fasta_Main.py
# Description: Initiator Set main script file
#
# Author: Jordan Eckhoff
# e-mail: jeckhoff@vulpinedesigns.com
#
# Contributors: N/A
# Contributor e-mails: N/A
#
# Creation Date:  10 Jul 2018
# Latest Version: 14 Jul 2018
#
# Usage Instructions: When prompted, open a .fa FASTA file. This file will ???

import IS_Fasta_Sequence # Custom module for working with FASTA files

from tkinter import Tk                         #
from tkinter.filedialog import askopenfilename # Asks user to select a .fa FASTA file
Tk().withdraw()                                #

with open(askopenfilename(),'r') as FastaFile: # Opens the selected .fa file via its PATH
    Sequences = IS_Fasta_Sequence.Sequence_Read(FastaFile.readlines()) # Creates a list of custom FASTA_Seq objects, each of which contains a single sequence from the FASTA file
                                                                       # and its associated metadata as seperate properties, Seq and Meta respectively, as well as Code, a string
                                                                       # indicating the type of sequence encoded (DNA, mRNA, Protein, or Indeterminable)

for a in range(0,len(Sequences)):
    print(Sequences[a].Meta + '\n',
    Sequences[a].Seq + '\n',
    Sequences[a].CodeType + '\n')

W = IS_Fasta_Sequence.Sequence_Translate(Sequences[0],1,'Protein')

print(W.Meta + '\n',
      W.Seq + '\n',
      W.CodeType + '\n')

X = IS_Fasta_Sequence.Sequence_Translate(Sequences[1],1,'Protein')

print(X.Meta + '\n',
      X.Seq + '\n',
      X.CodeType + '\n')

Y = IS_Fasta_Sequence.Sequence_Translate(Sequences[2],1,'Protein')

print(Y.Meta + '\n',
      Y.Seq + '\n',
      Y.CodeType + '\n')

Z = IS_Fasta_Sequence.Sequence_Translate(Sequences[3],1,'Protein')

<<<<<<< HEAD
print(Z.Meta + '\n',
      Z.Seq + '\n',
      Z.CodeType + '\n')
#
=======
print(Y.Meta + '\n',
      Y.Seq + '\n',
      Y.CodeType + '\n')
>>>>>>> e59d8e2a09a0425f9f0348e29065a88751b580f8
