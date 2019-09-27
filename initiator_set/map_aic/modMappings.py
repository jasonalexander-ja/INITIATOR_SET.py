# modMappings.py
#
# Utility for editing the codonWeights.dat file
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)


import sys
import argparse
from struct import *
from util.mRNA import *
try:
	m_file = open('codonWeights.dat','r+b')
except OSError as e:
	print("\"codonWeights.dat\" not found!\n"
		+ "Constructing new file...", file=sys.stderr)
	m_file = open('codonWeights.dat','x+b')
	m_file.write(bytearray(pack('<' + 'd'*64, *([0.0]*64))))


parser = argparse.ArgumentParser(description="A helper utility for populating "
    + "the \"codonWeights.dat\" file"
    , epilog="File Formatting Example:\n\nAUG 1000\nCUG 140\nAUC 15.3"
    , formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('infile', nargs='*', type=argparse.FileType('r')
	, help="Read weights stored in a file and update \"codonWeights.dat\" with "
	+ "the new data. Leave empty to print out currently stored data")


args = parser.parse_args()



if args.infile == []:
	for i in range(64):
		print(codonIndex(i) + " ", *unpack('<d', m_file.read(8)))
	sys.exit()



for n_file in args.infile:
	while True:
		codon = n_file.read(4)
		if codon == None or codon == "":
			break
		m_file.seek(indexCodon(codon) * 8)
		m_file.write(bytearray(pack('<d', float(n_file.readline()))))
