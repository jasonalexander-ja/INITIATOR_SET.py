from initiator_set.kozak_calculator.kozak_calculator import *
from initiator_set.map_aic import *
from initiator_set.map_aic.mapAIC import *
from initiator_set.kozak_calculator.kozak_loader import *
from initiator_set.leaky_scan_detector.leaky_scan_detector import *

mrna = mRNA("GCCGCCACCCUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA")

with open("../kozak_calculator/sample_kozaks.txt") as inz:
    kozaks = interpret_kozak_file(inz)
    mapAICs(mrna)
    calculate_kozaks(mrna, kozaks)


def test_penalty(distto5: int) -> float:
    return 1.0 if distto5 < 30 else 0.0


calculate_leaky(mrna)

print(mrna.metadata.__str__().replace(", '", "\n"))
print(is_leaky(mrna))
