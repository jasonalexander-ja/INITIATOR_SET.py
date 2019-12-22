# Helper utility for loading util directory. Python sucks at this so
# we need one of these in every folder which needs access to anything
# in a higher or adjacent directory.
import os
import sys
mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(mypath + '/../'))

