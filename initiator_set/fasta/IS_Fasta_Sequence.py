# Title: IS_Fasta_Sequence.py
# Description: Initiator Set FASTA analysis Classes & functions
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
# Usage Instructions: N/A - User does not interface with this file
#
# Information: The classes/functions in this file are designed for reading and basic analysis of the sequences within FASTA-format files

from tkinter import messagebox

class FASTA_Seq():
    # Has three properties:
    #   Meta - List of the metadata strings before the sequence strings, information within varies by FASTA standard
    #   Seq - List of the DNA, mRNA, or Amino Acid letter sequences
    #   CodeType - a string indicating the type of FASTA code
    def __init__(self, M, C, T):       
        self.Meta = M
        self.Seq = C
        self.CodeType = T



def Sequence_Read(FastaLines):
    # This function is for the intitial reading of a FASTA file, and storage of the data within in custom FASTA_Seq objects
    # Input args:
    #   FastaLines - A line-by-line list created from a FASTA file by readlines()
    # Output: Sequences, a list of FASTA_Seq objects
    Sequences = [FASTA_Seq('','','') for a in range(len(FastaLines))]
    CodeNo = 0
    for a in range(0,len(FastaLines)):
        if '>' in FastaLines[a]: # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
            CodeNo += 1
            Sequences[CodeNo].Meta += FastaLines[a][1:].replace('\n', '').replace('\r', '')
        else:
            Sequences[CodeNo].Seq += FastaLines[a].replace('\n', '').replace('\r', '') # Cuts empty spaces and line delimiter characters from the string line, then adds the line to the latest entry in the appropriate list
            
            if any(i in Sequences[CodeNo].Seq for i in ['B','G']):
                Sequences[CodeNo].CodeType = 'DNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['U']):
                Sequences[CodeNo].CodeType = 'mRNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['E','F','I','L','P','Q']): # Determines sequence type based on the presence of letters unique to either the Nucleotide or Protein FASTA format alphabets, with U as an identifier for mRNA
                Sequences[CodeNo].CodeType = 'Protein'
            else:
                Sequences[CodeNo].CodeType = 'Indeterminable'
    return Sequences[1:CodeNo+1]



def Sequence_Forward_Translate(Sequence,FrameNo=0,DesiredType='Protein'):
    # This function takes an individual FASTA_Seq object, and translates from DNA -> mRNA -> Protein
    # Input args:
    #   Sequence - A single FASTA_Seq object
    #   FrameNo - (Optional, defaults to 0) - Codon reading frame number. Can be any integer, but will be converted to 0, 1, or 2 by absolute value and modulo, 0 meaning reading frame starts from the first "letter" in a nucleotide sequence, followed by the second with 1, and the third with 2
    #   DesiredType - (Optional, defaults to 'Protein') - A string indicating the desired FASTA_Seq.CodeType for the sequence to be converted to over the course of this function. See Sequence_Read above for the 4 valid inputs. Invalid inputs or a DesiredType that is in the incorrect order (Inputting "DNA" when the sequence is already of type "Protein", for example), will cause the function to not return anything, thus the resulting error will call attention to the mistake.
    # Output: Sequence - The changed FASTA_Seq object

    FrameNo = abs(FrameNo % 3)
            
    if Sequence.CodeType == 'DNA': # DNA to mRNA conversion
        SequenceString = ''
        for b in range(0,len(Sequence.Seq)):
            if Sequence.Seq[b] == 'A':
                Nucleotide = 'U'
            elif Sequence.Seq[b] == 'C':
                Nucleotide = 'G'
            elif Sequence.Seq[b] == 'G':
                Nucleotide = 'C'
            elif Sequence.Seq[b] == 'T':
                Nucleotide = 'A'
            SequenceString += Nucleotide
        Sequence.Seq = SequenceString
        Sequence.CodeType = 'mRNA'

        if DesiredType == 'mRNA':
            return Sequence
            
    if Sequence.CodeType == 'mRNA': # mRNA to Protein conversion
        PeptideString = ''
        M_is_Start = True # Prevents Methionines after the START and before a STOP being tagged as extraneous STARTs
        Check_for_Stop = False # Prevents extraneous STOP characters from being added, as they are only for readability and not an actual Amino Acid
        for b in range(FrameNo,len(Sequence.Seq)-2,3):
            Codon = Sequence.Seq[b] + Sequence.Seq[b+1] + Sequence.Seq[b+2] # Stores each codon conforming to the selected reading frame into a temporary variable
            
            if Codon in ['CGA','CGG','CGU','CGC']: # Massive if-elif statement to convert each mRNA codon into an Amino Acid. Due to my use of [ and ] to denote Start and Stop codons, the sequence is no longer FASTA-standard past this point.
                AminoAcid = 'A'
            elif Codon in ['ACA','ACG']:
                AminoAcid = 'C'
            elif Codon in ['CUA','CUG']:
                AminoAcid = 'D'
            elif Codon in ['CUU','CUC']:
                AminoAcid = 'E'
            elif Codon in ['AAA','AAG']:
                AminoAcid = 'F'
            elif Codon in ['CCA','CCG','CCU','CCC']:
                AminoAcid = 'G'
            elif Codon in ['GUA','GUG']:
                AminoAcid = 'H'
            elif Codon in ['UAA','UAG']:
                AminoAcid = 'I'
            elif Codon in ['UUU','UUC']:
                AminoAcid = 'K'
            elif Codon in ['AAU','AAC','GAA','GAG','GAU','GAC']:
                AminoAcid = 'L'
            elif Codon in ['UAU','UAC']:
                if M_is_Start == True:
                    AminoAcid = '[M'
                    M_is_Start = False
                    Check_for_Stop = True
                else:
                    AminoAcid = 'M'
            elif Codon in ['UUA','UUG']:
                AminoAcid = 'N'
            elif Codon in ['GGA','GGG','GGU','GGC']:
                AminoAcid = 'P'
            elif Codon in ['GUU','GUC']:
                AminoAcid = 'Q'
            elif Codon in ['GCA','GCG','GCU','GCC','UCU','UCC']:
                AminoAcid = 'R'
            elif Codon in ['AGA','AGG','AGU','AGC','UCA','UCG']:
                AminoAcid = 'S'
            elif Codon in ['UGA','UGG','UGU','UGC']:
                AminoAcid = 'T'
            elif Codon in ['CAA','CAG','CAU','CAC']:
                AminoAcid = 'V'
            elif Codon in ['ACC']:
                AminoAcid = 'W'
            elif Codon in ['AUA','AUG']:
                AminoAcid = 'Y'
            elif Codon in ['AUU','AUC','ACU']:
                if Check_for_Stop == True:
                    AminoAcid = ']'
                    M_is_Start = True
                    Check_for_Stop = False
                else:
                    AminoAcid = ''
            else:
                AminoAcid = '?'
            PeptideString += AminoAcid
        Sequence.Seq = PeptideString
        Sequence.CodeType = 'Protein'

        if DesiredType == 'Protein':
            return Sequence
           
    if Sequence.CodeType == 'Protein': # Protein to ??? conversion, at this point in development there is no further conversion
        pass
        
    if Sequence.CodeType == 'Indeterminable': # Error message if Sequence_Read was unable to determine if the original sequence was a Nucleotide or Protein sequence, will only happen in very rare/improbable cases
        messagebox.showerror('Sequence Translation Error','Cannot translate sequence of indeterminable type')
    
