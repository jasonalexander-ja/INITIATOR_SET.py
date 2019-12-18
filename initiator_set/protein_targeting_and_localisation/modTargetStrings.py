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
	m_file = open(filename,'+')
except OSError as e:
	print("\"" + filename + "\" not found!\n"
		+ "Constructing new file...", file=sys.stderr)
	m_file = open(filename,'w')
	newfile = 1


parser = argparse.ArgumentParser(description="A helper utility for populating "
  + "the \"" + filename + "\" file", fromfile_prefix_chars='@'
  , formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('sequence', nargs='*', help="Add \"sequence\" to the datafile"
  , dest='toadd')

parser.add_argument('-r', '--remove', action='append', help="Instead of adding"
	+ ", remove from the datafile", dest='toremove')

parser.add_argument('-p', '--print-args', dest="print", action='store_true')

args = parser.parse_args()


filedata = m_file.readlines()
for seq in toadd:
	tmp = indexAminoChain(seq)
  


if args.print:
	m_file.read()
	sys.exit()
