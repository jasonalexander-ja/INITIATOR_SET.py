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
filename = os.path.abspath(mypath + 'locStrings.dat')


try:
	m_locstrings = open(filename, 'rb')
except OSError as e:
	print("[!!FATAL!!] Error opening \"locStrings.dat\"\n", file=sys.stderr)
	raise



#TODO
def tagLocStrings(aac:AminoAcidChain) -> AminoAcidChain:
	return aac;
