import os
from repackage import up
up() # required to make python start searching modules from the parent directory
from util.mRNA import mRNA
from kozak_calculator.kozak_calculator import calculate_kozaks
from kozak_calculator.kozak_loader import interpret_kozak_file

mrna = mRNA("GCCGCCACCAUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA")

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "sample_kozaks.txt")) as inz:
    kozaks = interpret_kozak_file(inz)
    calculate_kozaks(mrna, kozaks)


print(mrna.Metadata.__str__().replace(", '", "\n"))


