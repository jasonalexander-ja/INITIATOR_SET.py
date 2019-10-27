# modTargetStrings.py
#
# Utility for editing the locStrings.dat file
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)



import sys
import os
from __init__ import *
import argparse
from struct import pack, unpack
import util.AminoChain
filename = os.path.abspath(mypath + 'locStrings.dat')


try:
	m_file = open(filename,'+b')
except OSError as e:
	print("\"" + filename + "\" not found!\n"
		+ "Constructing new file...", file=sys.stderr)
	m_file = open(filename,'wb')
	newfile = 1


parser = argparse.ArgumentParser(description="A helper utility for populating "
    + "the \"" + filename + "\" file"
    , epilog="File Formatting Example:\n\nAUG 1000\nCUG 140\nAUC 15.3" #TODO
    , formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('infile', nargs='*', type=argparse.FileType('r') #TODO
	, help="Read strings stored in a file and update \"" + filename + "\" with "
	+ "the new data. Leave empty to print out currently stored data")


args = parser.parse_args()



if args.infile == []:
	if newfile:
		sys.exit()
	while m_file.readable():
		print(deindexAminoChain(*unpack('<c', m_file.read(8))) + '\n')
	sys.exit()


m_file.seek(0, SEEK_END)
for n_file in args.infile:
	while n_file.readable():
		seq = indexAminoChain(n_file.readline())
		for i in seq:
			m_file.write(bytearray(pack('<c', i)))
