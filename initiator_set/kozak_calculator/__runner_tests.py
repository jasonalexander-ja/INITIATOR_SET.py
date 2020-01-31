from initiator_set.kozak_calculator.kz_calculator_runner import *
from initiator_set.map_aic_alternative.aic_weights_loader import *
from initiator_set.kozak_calculator.kozak_loader import *

mrna = mRNA("GCCGCCACCAUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA")

with open("sample_kozaks.txt") as inz:
    with open("../map_aic_alternative/example_input.txt") as inf:
        kozaks = interpret_kozak_file(inz)
        weights = interpret_aic_weights(inf)
        map_aic(mrna, weights)
        calculate_kozaks(mrna, kozaks)


print(mrna.metadata.__str__().replace(", '", "\n"))


