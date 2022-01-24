# mRNA.py
#
# A representation of mRNA strand with a slew of metadata and utils for working
# with it
#
# Authored by: Lucianna Osucha (lucianna@vulpinedesigns.com)
from PyQt5.QtGui import QColor

bases = ['A', 'U', 'G', 'C']
nucleotideTextFormat = []
codonColors = []

for i in range(64):  # 64 codons, Hue step = 360/72
    codonColors.append(QColor.fromHsv(i * 5, 255, 255, 64))
    nucleotideTextFormat.append('<span style=\"background-color:' + \
                                str(codonColors[i].name(QColor.HexArgb)) + ';font-size:12px;\">')
# For Proteins, it has 21 standard colors


def deindexCodon(index: int) -> str:
    result = bases[int(index / 16)]
    result += bases[int((index / 4)) % 4]
    result += bases[index % 4]
    return result


def deindexRNA(code: list) -> str:
    result = ''
    for i in range(0, len(code), 3):
        result = result + deindexCodon(code[i])

    i = (len(code) - 1) % 3
    if i != 0:
        result = result + deindexCodon(code[-1])[-i:]
    return result


def indexCodon(codon: str) -> int:
    result = bases.index(codon[0]) * 16
    result += bases.index(codon[1]) * 4
    result += bases.index(codon[2])
    return result


def indexRNA(code: str) -> list:
    result = []
    for i in range(len(code) - 2):
        result.append(indexCodon(code[i:i + 3]))
    return result


class mRNA:
    def __init__(self, identification, cd):
        if isinstance(cd, str):
            code = indexRNA(cd)
        if not isinstance(code, list):
            raise TypeError("'code' must be of type 'str' or 'list'")

        self.Id = identification
        self.Nucleotide: list = cd
        self.Code: list = code
        self.Metadata: dict = {}

    def __str__(self) -> str:
        return deindexRNA(self.Code) + "\n" + str(self.Metadata['baseWeights']) + "\n" + str(
            self.Metadata['adjustedWeights'])


class Iterable(mRNA):

    def __init__(self, parent: mRNA, start: int, stop: int):

        self.parent: mRNA = parent
        self.loc: int = start - 3
        if stop <= start or stop > len(parent.Code):
            self.stop = len(parent.Code)
        else:
            self.stop: int = stop

    def __iter__(self):
        return self

    def next(self):
        self.loc += 3
        if self.loc >= self.stop:
            raise StopIteration

        value = self.parent.Code[self.loc:(self.loc + 3)]
        return value
