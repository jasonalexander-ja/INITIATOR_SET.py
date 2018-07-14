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
    #   Seq - List of the DNA, mRNA, or Amino Acid letter sequences
    #   Code - a string indicating the type of FASTA code
    def __init__(self, M, C, T):       
        self.Meta = M
        self.Seq = C
        self.Code = T



def Sequence_Read(FastaLines):
    for a in range(0,len(FastaLines)): # Runs through the FASTA file and creates a new entry in each list for each sequence's metadata and letter sequence
        CodeType = 'Indeterminable'
        ActualData = ['']
        MetaData = ['']
        x = ['']
        if '>' in FastaLines[a]: # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
            if ActualData[-1] != '':  # If the previous entry is not blank, a new blank entry is created for the list for the opposite type of data from what was found
                ActualData.append('') # FASTA files only have single metadata lines at a time (As far as the author knows), so this check is not as important for ActualData as it is for MetaData below, but I wanted uniformity in this statement, just in case
            MetaData[-1] += FastaLines[a].replace('\n', '').replace('\r', '')   # Cuts empty spaces and line delimiter characters from the string line, then adds the line to the latest entry in the appropriate list
            if any(i in MetaData[-1] for i in ['B','G']):
                CodeType = 'DNA'
            if any(i in MetaData[-1] for i in ['U']):
                CodeType = 'mRNA'
            if any(i in MetaData[-1] for i in ['E','F','I','L','P','Q']):
                CodeType = 'Protein'
        else:
            ActualData[-1] += FastaLines[a].replace('\n', '').replace('\r', '')
            if MetaData[-1] != '':
                MetaData.append('')

        x.append(FASTA_Seq(MetaData[-1],ActualData[-1],CodeType)) # The fact that a code line is read last causes MetaData to be one entry longer than it needs to be
    return x[1:len(x)]

#def Sequence_Type_Finder(Sequences):
