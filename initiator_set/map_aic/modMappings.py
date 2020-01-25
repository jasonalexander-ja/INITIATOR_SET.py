# modMappings.py
#
# Utility for editing the codonWeights.dat file
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)


from __init__ import *
import sys
import argparse
from struct import *
from util import mRNA
filename = mypath + '/codonWeights.dat'


try:
	m_file = open(filename,'+wb') # update binary file
except OSError as e:
	print("\"" + filename + "\" not found!\n"
		+ "Constructing new file...", file=sys.stderr)
	m_file = open(filename,'x+b') # create and update bytecode file
	# Pack 64 little endian floats, all set to 0.0, into a bytearray and
	# write to the file
	m_file.write(bytearray(pack('<' + 'f'*64, *([0.0]*64))))
	sys.exit()


parser = argparse.ArgumentParser(description="A helper utility for populating "
    + "the \"" + filename + "\" file"
    , epilog="For an example of the file format, run the program without any "
		+ "arguments (line order can be arbitrary, no upper or lower limit on "
		+ "file size). New entries or later entries in the file override older ones"
		, formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('infile', nargs='*', type=argparse.FileType('r')
	, help="Read weights stored in a file and update \""+ filename + "\" with "
	+ "the new data. Leave empty to print out currently stored data")


args = parser.parse_args()


# If empty, print the current weights in the same format they are input
if args.infile == []:
	for i in range(64):
		print(mRNA.deindexCodon(i) + " ", *unpack('<f', m_file.read(4)))
	sys.exit()



for n_file in args.infile:
	while True:
		codon = n_file.read(4)
		if codon == None or codon == "":
			break
		# Index RNA and use this value to find desired entry in datafile
		m_file.seek(mRNA.indexCodon(codon) * 4)
		# Pack weight into a little-endian float and write
		m_file.write(bytearray(pack('<f', float(n_file.readline()))))
