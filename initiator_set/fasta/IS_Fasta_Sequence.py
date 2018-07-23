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
    #   CodeType - a string indicating the type of FASTA code
    def __init__(self, M, C, T):       
        self.Meta = M
        self.Seq = C
        self.CodeType = T



def Sequence_Read(FastaLines):
    Sequences = [FASTA_Seq('','','') for a in range(len(FastaLines))]
    CodeNo = 0
    for a in range(0,len(FastaLines)):
        if '>' in FastaLines[a]: # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
            CodeNo += 1
            Sequences[CodeNo].Meta += FastaLines[a].replace('\n', '').replace('\r', '')
        else:
            Sequences[CodeNo].Seq += FastaLines[a].replace('\n', '').replace('\r', '') # Cuts empty spaces and line delimiter characters from the string line, then adds the line to the latest entry in the appropriate list
            
            if any(i in Sequences[CodeNo].Seq for i in ['B','G']):
                Sequences[CodeNo].CodeType = 'DNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['U']):
                Sequences[CodeNo].CodeType = 'mRNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['E','F','I','L','P','Q']):
                Sequences[CodeNo].CodeType = 'Protein'
            else:
                Sequences[CodeNo].CodeType = 'Indeterminable'
    return Sequences[1:CodeNo+1]



def Sequence_Translate(Sequence,FrameNo,DesiredType):
    FrameNo = FrameNo % 3
    NucleoSequence = ['']*len(Sequence.Seq)
        
    for a in range(0,len(Sequence.Seq)):
        NucleoSequence[a] = Sequence.Seq[a]
            
    if Sequence.CodeType == 'DNA':
        SequenceString = ''
        for b in range(0,len(NucleoSequence)):
            if NucleoSequence[b] == 'A':
                NucleoSequence[b] = 'U'
            elif NucleoSequence[b] == 'C':
                NucleoSequence[b] = 'G'
            elif NucleoSequence[b] == 'G':
                NucleoSequence[b] = 'C'
            elif NucleoSequence[b] == 'T':
                NucleoSequence[b] = 'A'
            SequenceString += NucleoSequence[b]
        Sequence.Seq = SequenceString
        Sequence.CodeType = 'mRNA'
        if DesiredType == 'mRNA':
            return Sequence
            
    if Sequence.CodeType == 'mRNA':
        CodonString = ''
        CodonSequence = ['']*(len(NucleoSequence)//3)
        SequenceString = ''
        c = 0
        for b in range(FrameNo,len(NucleoSequence)-2,3):
            CodonSequence[c] = NucleoSequence[b] + NucleoSequence[b+1] + NucleoSequence[b+2]
            if CodonSequence[c] in ['GCU','GCC','GCA','GCG']:
                CodonSequence[c] = 'A'
            elif CodonSequence[c] in ['UGU','UGC']:
                CodonSequence[c] = 'C'
            elif CodonSequence[c] in ['GAU','GAC']:
                CodonSequence[c] = 'D'
            elif CodonSequence[c] in ['GAA','GAG']:
                CodonSequence[c] = 'E'
            elif CodonSequence[c] in ['UUU','UUC']:
                CodonSequence[c] = 'F'
            elif CodonSequence[c] in ['GGU','GCC','GCA','GCG']:
                CodonSequence[c] = 'G'
            elif CodonSequence[c] in ['CAU','CAC']:
                CodonSequence[c] = 'H'
            elif CodonSequence[c] in ['AUU','AUC']:
                CodonSequence[c] = 'I'
            elif CodonSequence[c] in ['AAA','AAG']:
                CodonSequence[c] = 'K'
            elif CodonSequence[c] in ['UUA','UUG','CUU','CUC','CUA','CUG']:
                CodonSequence[c] = 'L'
            elif CodonSequence[c] in ['AUA','AUG']:
                CodonSequence[c] = '[M'
            elif CodonSequence[c] in ['AAU','AAC']:
                CodonSequence[c] = 'N'
            elif CodonSequence[c] in ['CCU','CCC','CCA','CCG']:
                CodonSequence[c] = 'P'
            elif CodonSequence[c] in ['CAA','CAG']:
                CodonSequence[c] = 'Q'
            elif CodonSequence[c] in ['CGU','CGC','CGA','CGG','AGA','AGG']:
                CodonSequence[c] = 'R'
            elif CodonSequence[c] in ['UCU','UCC','UCA','UCG','AGU','AGC']:
                CodonSequence[c] = 'S'
            elif CodonSequence[c] in ['ACU','ACC','ACA','ACG']:
                CodonSequence[c] = 'T'
            elif CodonSequence[c] in ['GUU','GUC','GUA','GUG']:
                CodonSequence[c] = 'V'
            elif CodonSequence[c] == 'UGG':
                CodonSequence[c] = 'W'
            elif CodonSequence[c] in ['UAU','UAC']:
                CodonSequence[c] = 'Y'
            elif CodonSequence[c] in ['UAA','UAG','UGA']:
                CodonSequence[c] = ']'
            else:
                CodonSequence[c] = '?'
            CodonString += CodonSequence[c]
            c += 1
        Sequence.Seq = CodonString
        Sequence.CodeType = 'Protein'
        
    if DesiredType == 'Protein':
        return Sequence
           
    if Sequence.CodeType == 'Protein':
        pass
        
    if Sequence.CodeType == 'Indeterminable':
       Sequence.Meta += ' ERROR'
            
    return Sequence
