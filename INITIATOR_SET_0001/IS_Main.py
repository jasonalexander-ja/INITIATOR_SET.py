import IS_Sequence

from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

FastaPath = askopenfilename()

with open(FastaPath,'r') as FastaFile:
    FastaLines = FastaFile.readlines()
    (MetaData,ActualData) = IS_Sequence.Splitter(FastaLines)
    Sequences = IS_Sequence.FASTA_Seq(MetaData,ActualData)
    print(Sequences.MetaData)
    print(Sequences.LetterCode)
