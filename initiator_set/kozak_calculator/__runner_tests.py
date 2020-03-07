from initiator_set.kozak_calculator.kozak_calculator import *
from initiator_set.kozak_calculator.kozak_loader import *

mrna = mRNA("GCCGCCACCAUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA")

with open("sample_kozaks.txt") as inz:
    kozaks = interpret_kozak_file(inz)
    calculate_kozaks(mrna, kozaks)


print(mrna.metadata.__str__().replace(", '", "\n"))


