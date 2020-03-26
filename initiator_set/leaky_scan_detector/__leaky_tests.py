import os

from repackage import up
up() # required to make python start searching modules from the parent directory
from kozak_calculator.kozak_calculator import calculate_kozaks
from kozak_calculator.kozak_loader import interpret_kozak_file
from leaky_scan_detector.leaky_scan_detector import calculate_leaky, is_leaky
from map_aic.mapAIC import mapAICs
from util.mRNA import mRNA

mrna = mRNA("GCCGCCACCCUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA")

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "kozak_calculator", "sample_kozaks.txt")) as inz:
    kozaks = interpret_kozak_file(inz)
    mapAICs(mrna)
    calculate_kozaks(mrna, kozaks)


def test_penalty(distto5: int) -> float:
    return 1.0 if distto5 < 30 else 0.0


calculate_leaky(mrna)

print(mrna.metadata.__str__().replace(", '", "\n"))
print(is_leaky(mrna))
