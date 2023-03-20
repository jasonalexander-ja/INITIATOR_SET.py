""" File: main.py

This file processes GUI for Initiator-Set-Module

Author: Son Nguyen
e-mail: snguyen@vulpinedesigns.com

Version: v0.1

Creation Date:  10 March 2021
"""

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QErrorMessage
import fasta.FastaSeq as fa
from gui.InitiatorSetGui import Ui_MainWindow
from kozak_calculator.kozak_calculator import calculate_kozaks
from kozak_calculator.kozak_loader import interpret_kozak_file
from leaky_scan_detector.leaky_scan_detector import is_leaky, calculate_leaky
from map_aic.mapAIC import loadCodonWeightsFromInputFile, mapAICs
from util.mRNA import indexCodon, deindexCodon, mRNA, nucleotideTextFormat, codonColors
from qt_material import apply_stylesheet
# import platform
# os = platform.uname()[0]
# # print(os)
# if os == 'Linux':
#     Ui_MainWindow = uic.loadUiType('/gui/InitiatorSetGui.ui')[0]
# elif os == 'Windows':
#     Ui_MainWindow = uic.loadUiType('gui\InitiatorSetGui.ui')[0]

mRNASequences = [mRNA('init', 'AUGC')]
kozaks = None
codonWeights = None
codonAdjustedWeights = None
leakyThreshold = None
#dispMapAics = True
class AppGUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.displayMapAICsResult_clicked(True)
        dispMapAics = True
    def calculateLeaky_clicked(self):
        global leakyThreshold
        try:
            calculate_leaky(mRNASequences[0])
            if leakyThreshold is None:
                print("Enter a Leaky threshold!")
                leakyThreshold = 0.1
                self.showThresholdLeaky.setText(str("%.3f" % leakyThreshold))

            isLeaky = str(is_leaky(mRNASequences[0], leakyThreshold))
            self.showIsLeaky.setText(isLeaky)
        # TODO use something other than value error, the other potential problems are ambigious with this error
        except ValueError as e:
            error_msg = QErrorMessage(self)
            error_msg.setWindowTitle("Error while Leaky Scanning")
            error_msg.showMessage("Cannot calculate Leaky Scanning :\n" + str(e))
            print(e)

    def translateToProteins_clicked(self):
        tableWidgetProtein = self.showTableWidgetProteins
        tableWidgetProtein.clearContents()
        kzContexts = mRNASequences[0].Metadata.get("kozakContexts")
        kzContextLength = len(kzContexts)
        self.showTableWidgetProteins.setRowCount(kzContextLength)
        self.showTableWidgetProteins.setColumnCount(2)
        mRNASequenceOrigin = mRNASequences[0].Nucleotide
        kzIndex = 0
        for kzCont in kzContexts:
            tableWidgetProtein.setItem(kzIndex, 0, QTableWidgetItem("Protein " + str(kzIndex + 1)))
            cutoffPos = kzCont.initiator_start
            newmRNASequence = fa.splitmRNASequence(mRNASequenceOrigin, cutoffPos)
            protein = fa.transmRNA2Protein(newmRNASequence)
            tableWidgetProtein.setItem(kzIndex, 1, QTableWidgetItem(protein.Seq))
            kzIndex += 1
        tableWidgetProtein.resizeColumnToContents(1)

    def updateLeakyThreshold(self, text):
        global leakyThreshold
        leakyThreshold = float(text)

    def itemChangedMapAICs_clicked(self, item: QTableWidgetItem):
        global codonWeights, codonAdjustedWeights
        codon = self.tableWidgetMapAICs.item(item.row(), 0).text()
        codonWeights[indexCodon(item.text(codon))] = item.text()
        # mRNASequences[0].
        # print(item.text(), " ", item.row(), " ", item.column())
        self.showTableWidgetMapAICs(codonWeights, codonAdjustedWeights)

    def calculateAdjustedWeights(self):
        global codonWeights, codonAdjustedWeights
        # Find max weight
        w_max = 0
        for i in codonWeights:
            if i > w_max:
                w_max = i

        # adjusted_weights = [0.00] * 64
        for i in range(0, len(codonWeights)):
            try:
                codonAdjustedWeights[i] = codonWeights[i] / w_max
            except ZeroDivisionError:
                codonAdjustedWeights[i] = 0.00

    def saveMapAICsData_clicked(self):
        global codonWeights, codonAdjustedWeights
        tableWidget = self.tableWidgetMapAICs
        rowNumber = tableWidget.rowCount()
        columnNumber = tableWidget.columnCount()
        for r in range(0, rowNumber):
            codonWeights[indexCodon(tableWidget.item(r, 0).text())] = float(tableWidget.item(r, 1).text())
        self.calculateAdjustedWeights()
        self.showTableWidgetMapAICs()

    def resetMapAICsData_clicked(self):
        pass

    def analyzeKozakContext_clicked(self):
        if kozaks is not None:
            calculate_kozaks(mRNASequences[0], kozaks)
            self.showProtein.setText(mRNASequences[0].Metadata.__str__().replace(", '", "\n"))
            self.showmRNA.setText(self.colorKozakContexts())
            # mRNASequences[0].Nucleotide,
            #                                           mRNASequences[0].Metadata.get("kozakContexts"),
            #                                           kozaks[0].sequence))
        else:
            error_msg = QErrorMessage(self)
            error_msg.setWindowTitle("No Data")
            error_msg.showMessage("There is no Kozak data to analyze with")

    def selectKozakData_clicked(self):
        options = QFileDialog()
        (inputFileName, _) = QFileDialog.getOpenFileName(self, "Select Kozak File", "", "All Files (*)",
                                                options=options)
        if inputFileName != '':
            try:
                with open(inputFileName, 'r') as kozak_infile:
                    global kozaks
                    try:
                        kozaks = interpret_kozak_file(kozak_infile)
                        self.tableWidgetKozak.clearContents()
                        self.tableWidgetKozak.setRowCount(6)
                        sequenceLength = len(kozaks[0].sequence)
                        startCodonPos = kozaks[0].codonStart
                        self.tableWidgetKozak.setColumnCount(sequenceLength)
                        headerLabels = []
                        for pos in range(0, sequenceLength):
                            if pos < startCodonPos:
                                headerLabels.append(str(-startCodonPos + pos) + " pos")
                            else:
                                headerLabels.append("+" + str(-startCodonPos + pos + 1) + " pos")
                            self.tableWidgetKozak.setItem(0, pos, QTableWidgetItem(str(kozaks[0])[pos]))
                            self.tableWidgetKozak.setItem(1, pos, QTableWidgetItem(str("%.3f" % kozaks[0].sequence[pos].importance)))
                            self.tableWidgetKozak.setItem(2, pos, QTableWidgetItem(str("%.3f" % kozaks[0].sequence[pos].a)))
                            self.tableWidgetKozak.setItem(3, pos, QTableWidgetItem(str("%.3f" % kozaks[0].sequence[pos].u)))
                            self.tableWidgetKozak.setItem(4, pos, QTableWidgetItem(str("%.3f" % kozaks[0].sequence[pos].g)))
                            self.tableWidgetKozak.setItem(5, pos, QTableWidgetItem(str("%.3f" % kozaks[0].sequence[pos].c)))
                        self.tableWidgetKozak.setHorizontalHeaderLabels(headerLabels)
                        self.showConversed.setText(str("%.5f" % kozaks[0].conserved))
                        self.showConservedThreshold.setText(str("%.5f" % kozaks[0].conserved_threshold))
                    except ValueError as e:
                        error_msg = QErrorMessage(self)
                        error_msg.setWindowTitle("File Parse Error")
                        error_msg.showMessage("Cannot parse file " + inputFileName[0] + " as Kozak Consensus")
                        print(e)
            except OSError as e:
                error_msg = QErrorMessage(self)
                error_msg.setWindowTitle("File Not Found")
                error_msg.showMessage("File was specified, but program could not load it for some reason")
                print(e)



    def selectMapAICsData_clicked(self):
        global codonWeights, codonAdjustedWeights, mRNASequences
        options = QFileDialog().options()
        (inputFileName, _) = QFileDialog.getOpenFileName(self, "Select AIC Map Data", "", "All Files (*)",
                                              options=options)
        if inputFileName != '':
            try:
                with open(inputFileName, 'r') as inputFile: # with open('map_aic/another_input.txt', 'r') as inputFile:s
                    codonWeights, codonAdjustedWeights = loadCodonWeightsFromInputFile(inputFile)
                    self.showTableWidgetMapAICs()
            except ValueError as e:
                    error_msg = QErrorMessage(self)
                    error_msg.setWindowTitle("File Parse Error")
                    error_msg.showMessage("Cannot parse file " + inputFileName[0] + " as a Map AIC file. Check console for details")
                    print(e.with_traceback)
            except OSError as e:
                error_msg = QErrorMessage(self)
                error_msg.setWindowTitle("File Not Found")
                error_msg.showMessage("File was specified, but program could not load it for some reason")
                print(e)




    def showTableWidgetMapAICs(self):
        global codonWeights, codonAdjustedWeights
        for idx in range(0, len(codonWeights)):
            codon = QTableWidgetItem(deindexCodon(idx))
            codon.setBackground(codonColors[idx])
            self.tableWidgetMapAICs.setItem(idx, 0, codon)
            self.tableWidgetMapAICs.setItem(idx, 1, QTableWidgetItem(str("%.3f" % codonWeights[idx])))
            self.tableWidgetMapAICs.setItem(idx, 2, QTableWidgetItem(str("%.3f" % codonAdjustedWeights[idx])))
        self.tableWidgetMapAICs.sortByColumn(2, QtCore.Qt.DescendingOrder)

    def displayMapAICsResult_clicked(self, displayMapAICsResult: bool):
        global mRNASequences
        mRNASequences[0].Metadata["displayMapAICsResult"] = str(displayMapAICsResult)

    def colorCodonsByWeights(self, nucleotideSequence: list, codeSequennce: list, adjustedWeights: str) -> str:
        i = -1
        length = len(nucleotideSequence)  # add 2 because 2 last nucleotides don't need to check
        offset = 2
        while i >= -length + 2:
            
            if adjustedWeights[i] > 0:
                pos = i + 3  # move to the first nucleotide of this weighted codon
                if "<" in nucleotideSequence[:length + pos - offset]:
                    offset = offset+3
                    #print("OFFSET " +str(offset))                
                              
                #print(nucleotideSequence[:length + pos - offset]+"\n")
                nucleotideSequence = nucleotideSequence[:length + pos - offset] + \
                                     nucleotideSequence[length + pos - offset:] +"</span>"
#                                    "</span>" + nucleotideSequence[length + pos - offset:]
                nucleotideSequence = nucleotideSequence[:length + i - 2] + \
                                     nucleotideTextFormat[codeSequennce[length + i - 2]] + \
                                     nucleotideSequence[length + i - 2:]
            i -= 1
        #print("\n")
        print(nucleotideSequence)
        return nucleotideSequence

    def formatNucleotideText(self):
        pass

    def colorKozakContexts(self) -> str:
        # nucleotideSequence: list, kozakContexts: list, kozakImprotanceSequence: list) -> str:
        global kozaks
        nucleotideSequence = mRNASequences[0].Nucleotide
        length = len(mRNASequences[0].Nucleotide)  # add 2 because 2 last nucleotides don't need to check
        kozakContexts = mRNASequences[0].Metadata.get("kozakContexts")
        contextNumber = len(kozakContexts) - 1
        contextStart = kozakContexts[contextNumber].context_start
        contextEnd = kozakContexts[contextNumber].context_end
        i = length - 1
        while i >= 0:
            if contextEnd >= i and i > contextStart:
                nucleotideSequence = nucleotideSequence[:i] + \
                                     "</span>" + nucleotideSequence[i:]
                importance = kozaks[0].sequence[i - contextStart - 1].importance
                nucleotideSequence = nucleotideSequence[:i - 1] + \
                                     '<span style=\"background-color:' + \
                                     str(QColor.fromHsv(0, 255, 255, 20*(importance+2)).name(QColor.HexArgb)) + \
                                     ";font-size:" + \
                                     str(12 + importance) + "px\">" + \
                                     nucleotideSequence[i - 1:]

            if i == contextStart:
                contextNumber -= 1
                contextStart = kozakContexts[contextNumber].context_start
                contextEnd = kozakContexts[contextNumber].context_end
            i -= 1
        return nucleotideSequence

    def analyzeMapAICs_clicked(self):
        global mRNASequences
        # Process for the first mRNA in Sequences
        if codonWeights:
            mRNASequences[0] = mapAICs(mRNASequences[0], codonWeights)
            dispMapAics = mRNASequences[0].Metadata.get("displayMapAICsResult")
            
            if dispMapAics == 'True':
                self.showProtein.setText(str(mRNASequences[0].Metadata.get('adjustedWeights')))
                self.showmRNA.setText(self.colorCodonsByWeights(mRNASequences[0].Nucleotide,
                                                                mRNASequences[0].Code,
                                                                mRNASequences[0].Metadata.get("adjustedWeights")))
        else:
            error_msg = QErrorMessage(self)
            error_msg.setWindowTitle("No AIC weights")
            error_msg.showMessage("AIC weights not specified, load a file.")

    # TODO exception handling on open() needed?
    def openFastaFile_clicked(self):
        global mRNASequences
        options = QFileDialog().options()
        (fileName, _) = QFileDialog.getOpenFileName(self, "Select FASTA File", "", "All Files (*)",
                                            options=options)
        if fileName != '':
            try:
                with open(fileName, 'r') as file:
                    mRNASequences = fa.transDNA2mRNA(file)
                self.showmRNA.setText(mRNASequences[0].Id + "\n" + mRNASequences[0].Nucleotide)
            except OSError as e:
                error_msg = QErrorMessage(self)
                error_msg.setWindowTitle("File Not Found")
                error_msg.showMessage("File was specified, but program could not load it for some reason")
                print(e)
    # self.showProtein.setText(fastaProtein)


def main():
    app = QApplication(sys.argv)
    appGUI = AppGUI(None)
    appGUI.showMaximized()
    apply_stylesheet(app, theme='dark_teal.xml')
    exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
