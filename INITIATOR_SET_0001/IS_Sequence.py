# Title: IS_Sequence.py
# Description: Initiator Set FASTA analysis Classes & functions
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
# Usage Instructions: N/A - User does not interface with this file

class FASTA_Seq():
    def __init__(self, FastaLines):
        
        MetaData = ['']
        ActualData = ['']
        
        for a in range(0,len(FastaLines)):

            if FastaLines[a].find('>') != -1:
                ActualData.append('')
                MetaData[-1] += FastaLines[a].replace('\n', '').replace('\r', '')
            else:
                ActualData[-1] += FastaLines[a].replace('\n', '').replace('\r', '')
                MetaData.append('')

        if MetaData[0] == '':
            self.Meta = MetaData[1:len(MetaData)]
            self.Seq = ActualData[1:len(ActualData)]
        else:
            self.Meta = MetaData[0:len(MetaData)-1]
            self.Seq = ActualData[1:len(ActualData)]
