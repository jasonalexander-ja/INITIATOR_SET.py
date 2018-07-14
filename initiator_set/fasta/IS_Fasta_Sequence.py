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

class FASTA_Raw_Seq():
    # Has two properties:
    #   Meta - List of the metadata strings before the sequence strings, information within varies by FASTA standard
    #   Seq - List of the DNA, mRNA, or Amino Acid letter sequences
    # Corresponding indices of self.Meta and self.Seq will contain the metadata and letter sequence for a single entry in a FASTA file. If the file only has one entry, these will each be single strings
    def __init__(self, FastaLines):       
        MetaData = ['']
        ActualData = ['']        
        for a in range(0,len(FastaLines)): # Runs through the FASTA file and creates a new entry in each list for each sequence's metadata and letter sequence

            if FastaLines[a].find('>') != -1: # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
                if ActualData[-1] != '':  # If the previous entry is not blank, a new blank entry is created for the list for the opposite type of data from what was found
                    ActualData.append('') # FASTA files only have single metadata lines at a time (As far as the author knows), so this check is not as important for ActualData as it is for MetaData below, but I wanted uniformity in this statement, just in case
                MetaData[-1] += FastaLines[a].replace('\n', '').replace('\r', '')   # Cuts empty spaces and line delimiter characters from the string line,
            else:                                                                   #
                ActualData[-1] += FastaLines[a].replace('\n', '').replace('\r', '') # Then adds the line to the latest entry in the appropriate list
                if MetaData[-1] != '':  # See the comments 5 & 4 lines above here
                    MetaData.append('') #

            self.Meta = MetaData[0:len(MetaData)-1] # The fact that a code line is read last causes MetaData to be one entry longer than it needs to be
            self.Seq = ActualData[0:len(ActualData)]
