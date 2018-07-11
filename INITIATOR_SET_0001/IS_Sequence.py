class FASTA_Seq():
    def __init__(self, M, C):
        self.MetaData = M
        self.LetterCode = C

def Splitter(FastaLines):
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
        return (MetaData[1:len(MetaData)],ActualData[1:len(ActualData)])
    else:
        return (MetaData[0:len(MetaData)-1],ActualData[1:len(ActualData)])
