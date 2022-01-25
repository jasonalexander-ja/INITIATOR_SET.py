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
# Latest Version:  7 Aug 2018
#
# Usage Instructions: When prompted, open a .fa FASTA file. This file will ???

import IS_Fasta_Sequence  # Custom module for working with FASTA files

from tkinter import messagebox
from tkinter import Tk  #
from tkinter.filedialog import askopenfilename  # Asks user to select a .fa FASTA file

Tk().withdraw()  #

try:
    with open(askopenfilename(), 'r') as FastaFile:  # Opens the selected .fa file via its PATH
        Sequences = IS_Fasta_Sequence.Sequence_Read(FastaFile.readlines())
        # Creates a list of custom FASTA_Seq objects, each of which contains a single sequence from the FASTA file
        # and its associated metadata as seperate properties, Seq and Meta respectively, as well as Code, a string
        # indicating the type of sequence encoded (DNA, mRNA, Protein, or Indeterminable)

    print('There are ' + str(len(
        Sequences)) + ' sequences in this FASTA file.\n' + 'Please input which number sequence you would like to use:')
    SeqNo = int(input())
    print('\n')
    print('Selected sequence data:\n')
    print('   Metadata: ' + Sequences[SeqNo - 1].Id + '\n')
    print('   Original Sequence: ' + Sequences[SeqNo - 1].Seq + '\n')
    print('Please enter reading frame number (0, 1, or 2):')
    FrameNo = int(input())
    X = IS_Fasta_Sequence.Sequence_Forward_Translate(Sequences[SeqNo - 1], FrameNo)
    print('Translated Sequence: ' + X.Seq)

    for a in range(0, len(Sequences)):
        print(Sequences[a].Id + '\n',
              Sequences[a].Seq + '\n',
              Sequences[a].CodeType + '\n')

    # W = IS_Fasta_Sequence.Sequence_Forward_Translate(Sequences[0],2,'Protein')

    # print(W.Meta + '\n',
    #      W.Seq + '\n',
    #      W.CodeType + '\n')

    # X = IS_Fasta_Sequence.Sequence_Forward_Translate(Sequences[1],2,'Protein')

    # print(X.Meta + '\n',
    #      X.Seq + '\n',
    #      X.CodeType + '\n')

    # Y = IS_Fasta_Sequence.Sequence_Forward_Translate(Sequences[2],2,'Protein')

    # print(Y.Meta + '\n',
    #      Y.Seq + '\n',
    #      Y.CodeType + '\n')

    # Z = IS_Fasta_Sequence.Sequence_Forward_Translate(Sequences[3],2,'Protein')

    # print(Z.Meta + '\n',
    #      Z.Seq + '\n',
    #      Z.CodeType + '\n')
except FileNotFoundError:
    messagebox.showerror('File Selection Error', 'No file selected, please try again')
