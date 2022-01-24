# modMappings.py
#
# Utility for editing the codonWeights.dat file
#
# Author: Lucianna Osucha (email:lucianna@vulpinedesigns.com)
# To run:
# select an input file, ex: another_input.txt
# edit run configuration with parameter = E:/Documents/Volunteer/VulpineDesign/INITIATOR_SET-master/initiator_set/map_aic/another_input.txt
# Shift + F10 to run
# Why run terminal -> \INITIATOR_SET-master\initiator_set>python map_aic\modMappings.py map_aic\another_input.txt
# but error: No module named "util"


from __init__ import *
import sys
# indicates the parent directory of the current directory, which is the project directory of this project
# sys.path.append("../")  # This way suitable for project path change, must run at project folder\module
# sys.path.append('E:\\Documents\\Volunteer\\VulpineDesign\\INITIATOR_SET-master\\initiator_set')  # Can run any where
from repackage import up
up() # required to make python start searching modules from the parent directory
import os
import argparse
from struct import *
from util.mRNA import indexCodon, deindexCodon

mypath = os.path.dirname(os.path.abspath(__file__))  # This is Project Root

filename = mypath + '\codonWeights.dat'

# print(filename)

# Open the file, if possible
try:
    m_file = open(filename, 'rb')
# If no file, create it
# Edits by Akasha:
#   Switched from OSError to FileNotFoundError, because if the file was actually there but just
#   didn't load for some reason (e.g: linux permissions) it would just be deleted!!
except FileNotFoundError as e:
    m_file = open(filename, 'x+b')  # create and update bytecode file
    # Pack 64 little endian floats, all set to 0.0, into a bytearray and
    # write to the file
    m_file.write(bytearray(pack('<' + 'f' * 64, *([0.0] * 64))))
    m_file.close()
    m_file = open(filename, 'rb')
except OSError as e:
    print("Cannot open codonWeights.dat file", file=sys.stderr)
    sys.exit()

parser = argparse.ArgumentParser(description="A helper utility for populating "
                                             + "the \"" + filename + "\" file"
                                 , epilog="For an example of the file format, run the program without any "
                                          + "arguments (line order can be arbitrary, no upper or lower limit on "
                                       + "file size). New entries or later entries in the file override older ones"
                                 , formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('infile', nargs='*', type=argparse.FileType('r')
                    , help="Read weights stored in a file and update \"" + filename + "\" with "
                           + "the new data. Leave empty to print out currently stored data")

args = parser.parse_args()

# If arguments are empty, echo out the current codonWeights.dat and terminate program
if not args.infile:

    for i in range(64):
        print(deindexCodon(i) + " ", *unpack('<f', m_file.read(4)))
    m_file.close()
    sys.exit()

# Behavioural change from bug fix.
if len(args.infile) > 1:
    print("Multiple files not supported", file=sys.stderr)
    m_file.close()
    sys.exit()

# If contain arguments, update the codonWeights.dat
n_file = args.infile[0]

# This is the original code
# it does not work because whatever content after the last m_file.write() gets deleted!!

# while True:
# 	codon = n_file.read(4)
# 	if codon is None or codon == "":
# 		break
# 	# Index RNA and use this value to find desired entry in datafile
# 	m_file.seek(mRNA.indexCodon(codon) * 4)
# 	# Pack weight into a little-endian float and write
# 	m_file.write(bytearray(pack('<f', float(n_file.readline()))))
# m_file.seek(0, 2) # this didn't work sadly...
# m_file.close()

# Get all the weights in memory first
# This is needed so that the file is not overwritten in write mode,
# truncating all data past the last m_file.write() command
weights = [0.0] * 64

# copy over the values in the new file, into memory first
while True:
    codon = n_file.read(4)
    if codon is None or codon == "":
        break
    weights[indexCodon(codon)] = float(n_file.readline())

# Close the file and reopen in binary write mode to
# write the new weights (that are now in memory, overwrite the whole file)
m_file.close()
m_file = open(filename, '+wb')
for i in weights:
    m_file.write(bytearray(pack('<f', i)))

# Print out success message
print("codonWeights.dat file updated. Run without arguments to verify changes")
m_file.close()
# m_file = open(filename, 'rb')
# for i in range(64):
# 	print(mRNA.deindexCodon(i) + " ", *unpack('<f', m_file.read(4)))
# m_file.close()
