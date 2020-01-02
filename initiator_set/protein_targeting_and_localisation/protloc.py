# protloc.py
#
# <TODO: filedescription>
#
# Author: Lucianna Osucha (lucianna@vulpinedesigns.com)

import sys
import os
from __init__ import *
from util.AminoChain import *
from struct import *
filename = os.path.abspath(mypath + 'locStrings.txt')


try:
	m_locstrings = open(filename, 'r')
except OSError as e:
	print("[!!FATAL!!] Error opening \"" + filename + "\"\n", file=sys.stderr)
	raise



#TODO
def tagLocStrings(aac:AminoAcidChain) -> AminoAcidChain:
	return aac;
