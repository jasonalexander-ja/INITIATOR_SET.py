""" File: FastaSeq.py

This file processes all FASTA sequence functions
Inputs:
    An input Fasta sequence
    TransFastaConfig class: the way to transcription and/or translation the input Fasta sequence
Outputs:
    The input Fasta sequence (convert to text, for showing on Gui purpose)
    An output Fasta sequence (text) after processing by the TransFastaConfig

Author: Son Nguyen
e-mail: snguyen@vulpinedesigns.com

Contributors: Jordan Eckhoff

Creation Date:  14 Feb 2021
"""
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox
from util.mRNA import mRNA


#
# class Nucleotide:
#     def __init__(self, code: str, color=QColor("Black")):
#         self.Code: str = code
#         self.Color: QColor = color      # this field for display the nucleotide code only


class FastaStruct:
    # Has three properties:
    #   Id - List of the identification strings before the sequence strings, information within varies by FASTA standard
    #   Seq - List of all letters in sequence
    #   CodeType - a string indicating the type of FASTA code: DNA, mRNA, Protein or Indeterminable
    def __init__(self, M, C, T):
        self.Id = M
        self.Seq = C
        self.CodeType = T


def readSequence(FastaLines):
    # This function is for the initial reading of a FASTA file, and storage of the data within in
    # custom FASTA_Seq objects
    # Input args:
    #   FastaLines - A line-by-line list created from a FASTA file by readlines()
    # Output:
    #   Sequences, a list of FastaStruct objects, sequence length is equal line numbers in file,
    #   empty lines will be removed later
    Sequences = [FastaStruct('', '', '') for a in range(len(FastaLines))]
    CodeNo = -1
    for pos in range(0, len(FastaLines)):
        # Ignore empty lines
        if not FastaLines[pos].strip():
            continue
        if '>' in FastaLines[pos]:
            # Uses the starter character of a FASTA metadata line, >, to differentiate metadata from sequence lines
            CodeNo += 1
            Sequences[CodeNo].Id += FastaLines[pos][1:].replace('\n', '').replace('\r', '')
        else:
            Sequences[CodeNo].Seq += FastaLines[pos].replace('\n', '').replace('\r', '')
            # Cuts empty spaces and line delimiter characters from the string line, then adds the line to the latest
            # entry in the appropriate list
            # TODO: below logic checking need to improve with strict conditions
            if any(i in Sequences[CodeNo].Seq for i in ['T']):  # why ['B', 'G']?
                Sequences[CodeNo].CodeType = 'DNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['U']):
                Sequences[CodeNo].CodeType = 'mRNA'
            elif any(i in Sequences[CodeNo].Seq for i in ['E', 'F', 'I', 'L', 'P', 'Q']):
                # Determines sequence type based on the presence of letters unique to either the Nucleotide or
                # Protein FASTA format alphabets, with U as an identifier for mRNA
                Sequences[CodeNo].CodeType = 'Protein'
            else:
                Sequences[CodeNo].CodeType = 'Indeterminable'
    # Filter out empty data
    Sequences = list(filter(lambda seq: seq.Seq != '', Sequences))
    return Sequences


def translateSequenceForward(Sequence, FrameNo=0, DesiredType='Protein') -> []:
    # This function takes an individual FASTA_Seq object, and translates from DNA -> mRNA -> Protein
    # Input args:
    #    Sequence - A single FASTA_Seq object
    #    FrameNo - (Optional, defaults to 0) - Codon reading frame number. Can be any integer, but will be converted
    #    to 0, 1, or 2 by absolute value and modulo,
    #    0 meaning reading frame starts from the first "letter" in a nucleotide sequence, followed by the second with
    #    1, and the third with 2
    #
    #    DesiredType - (Optional, defaults to 'Protein') - A string indicating the desired FASTA_Seq.CodeType for the
    #    sequence to be converted to over the course of this function.
    #    See Sequence_Read above for the 4 valid inputs. Invalid inputs or a DesiredType that is in the incorrect order
    #    (Inputting "DNA" when the sequence is already of type "Protein",
    #    for example), will cause the function to not return anything, thus the resulting error will call attention to
    #    the mistake.
    # Output: Sequence - The changed FASTA_Seq object

    FrameNo = abs(FrameNo % 3)

    if Sequence.CodeType == 'DNA':  # DNA to mRNA conversion
        SequenceString = ''
        mNucleotide = ''
        for pos in range(0, len(Sequence.Seq)):
            if Sequence.Seq[pos] == 'A':
                mNucleotide = 'U'
            elif Sequence.Seq[pos] == 'C':
                mNucleotide = 'G'
            elif Sequence.Seq[pos] == 'G':
                mNucleotide = 'C'
            elif Sequence.Seq[pos] == 'T':
                mNucleotide = 'A'
            SequenceString += mNucleotide
        Sequence.Seq = SequenceString
        Sequence.CodeType = 'mRNA'

        if DesiredType == 'mRNA':
            return Sequence

    if Sequence.CodeType == 'mRNA':  # mRNA to Protein conversion
        PeptideString = ''
        M_is_Start = True  # Prevents Methionines after the START and before a STOP being tagged as extraneous STARTs
        Check_for_Stop = False  # Prevents extraneous STOP characters from being added, as they are only for readability
        # and not an actual Amino Acid
        for pos in range(FrameNo, len(Sequence.Seq) - 2, 3):
            Codon = Sequence.Seq[pos] + Sequence.Seq[pos + 1] + Sequence.Seq[
                pos + 2]  # Stores each codon conforming to the
            # selected reading frame into a temporary variable

            if Codon in ['GCU', 'GCC', 'GCA', 'GCG']:  # Massive if-elif statement to convert each mRNA codon into an
                # Amino Acid. Due to my use of [ and ] to denote Start and Stop codons, the sequence is no longer
                # FASTA-standard past this point.
                AminoAcid = 'A'
            elif Codon in ['UGU', 'UGC']:
                AminoAcid = 'C'
            elif Codon in ['GAU', 'GAC']:
                AminoAcid = 'D'
            elif Codon in ['GAA', 'GAG']:
                AminoAcid = 'E'
            elif Codon in ['UUU', 'UUC']:
                AminoAcid = 'F'
            elif Codon in ['GGU', 'GGC', 'GGA', 'GGG']:
                AminoAcid = 'G'
            elif Codon in ['CAU', 'CAC']:
                AminoAcid = 'H'
            elif Codon in ['AUU', 'AUC', 'AUA']:
                AminoAcid = 'I'
            elif Codon in ['AAA', 'AAG']:
                AminoAcid = 'K'
            elif Codon in ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']:
                AminoAcid = 'L'
            elif Codon in ['AUG']:
                if M_is_Start == True:
                    AminoAcid = '[M'
                    M_is_Start = False
                    Check_for_Stop = True
                else:
                    AminoAcid = 'M'
            elif Codon in ['AAU', 'AAC']:
                AminoAcid = 'N'
            elif Codon in ['CCU', 'CCC', 'CCA', 'CCG']:
                AminoAcid = 'P'
            elif Codon in ['CAA', 'CAG']:
                AminoAcid = 'Q'
            elif Codon in ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
                AminoAcid = 'R'
            elif Codon in ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']:
                AminoAcid = 'S'
            elif Codon in ['ACU', 'ACC', 'ACA', 'ACG']:
                AminoAcid = 'T'
            elif Codon in ['GUU', 'GUC', 'GUA', 'GUG']:
                AminoAcid = 'V'
            elif Codon in ['UGG']:
                AminoAcid = 'W'
            elif Codon in ['UAU', 'UAC']:
                AminoAcid = 'Y'
            elif Codon in ['UAA', 'UAG', 'UGA']:
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

    if Sequence.CodeType == 'Protein':  # Protein to ??? conversion, at this point in development there is no further
        # conversion
        pass

    if Sequence.CodeType == 'Indeterminable':  # Error message if Sequence_Read was unable to determine if the original
        # sequence was a Nucleotide or Protein sequence, will only happen in very rare/improbable cases
        QMessageBox.critical(None, 'Sequence Translation Error', 'Cannot translate sequence of indeterminable type')


def translateSequence2Protein(sequences, FrameNo=0, DesiredType='Protein'):
    return translateSequenceForward(sequences, FrameNo, DesiredType)


def transDNA2mRNA(fastaFile) -> [FastaStruct]:
    # Input: fastaFile can include many DNAs
    # Output: mRNASequences, a list of FastaStruct objects

    with fastaFile:
        sequences = readSequence(fastaFile.readlines())
        mRNAFastaSequences = []
        # fastaProtein = ''
        for seq in sequences:
            if seq.CodeType == 'DNA':
                mRNAFastaSequences.append(translateSequenceForward(seq, 0, 'mRNA'))
            # eachSeq = translateSequence(seq, 0, 'Protein')
            # fastaProtein += eachSeq.Meta + " - " + eachSeq.Seq + " - " + eachSeq.CodeType + '\n'

    mRNASequences = convert2mRNAStruct(mRNAFastaSequences)
    return mRNASequences


def convert2mRNAStruct(FastaStructSequences) -> []:
    mRNASequences = [mRNA(FastaStructSequences[i].Id, FastaStructSequences[i].Seq) for i in
                     range(len(FastaStructSequences))]
    return mRNASequences


def transmRNA2Protein(nucleotideSequence: str) -> str:
    mRNASeq = FastaStruct('Protein', nucleotideSequence, 'mRNA')
    protein = translateSequenceForward(mRNASeq, 0, "Protein")
    return protein


def splitmRNASequence(nucleotideSequence: str, cutoffPosition: int) -> str:
    if 0 >= cutoffPosition and cutoffPosition >= len(nucleotideSequence):
        print("Cannot cut mRNA sequence")
    else:
        nucleotideSequenceRight = nucleotideSequence[cutoffPosition:]
    return nucleotideSequenceRight
