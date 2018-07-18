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
# Latest Version: 14 Jul 2018
#
# Usage Instructions: N/A - User does not interface with this file



class FASTA_Seq():
    # Has three properties:
    #   Meta - List of the metadata strings before the sequence strings, information within varies by FASTA standard
    #   Sequence - List of the DNA, mRNA, or Amino Acid letter sequences
    #   CodeType - a string indicating the type of FASTA code
    def __init__(self, M, C, T):       
        self.Meta = M
        self.Sequence = C
        self.CodeType = T



def Sequence_Read(FastaLines):
    Sequences = [FASTA_Seq('','','') for a in range(len(FastaLines))]
    CodeNo = 0
    for a in range(0,len(FastaLines)):
        if '>' in FastaLines[a]: # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
            CodeNo += 1
            Sequences[CodeNo].Sequence += FastaLines[a].replace('\n', '').replace('\r', '')
        else:
            Sequences[CodeNo].Meta += FastaLines[a].replace('\n', '').replace('\r', '') # Cuts empty spaces and line delimiter characters from the string line, then adds the line to the latest entry in the appropriate list
            
            if any(i in Sequences[CodeNo].Meta for i in ['B','G']):
                Sequences[CodeNo].CodeType = 'DNA'
            elif any(i in Sequences[CodeNo].Meta for i in ['U']):
                Sequences[CodeNo].CodeType = 'mRNA'
            elif any(i in Sequences[CodeNo].Meta for i in ['E','F','I','L','P','Q']):
                Sequences[CodeNo].CodeType = 'Protein'
            else:
                Sequences[CodeNo].CodeType = 'Indeterminable'
    return Sequences[1:CodeNo+1]

#def Sequence_Type_Finder(Sequences):
