from initiator_set.map_aic_alternative.aic_weights_loader import interpret_aic_weights
from initiator_set.map_aic_alternative.map_aic import map_aic
from initiator_set.leaky_scan_detector.leaky_scan_simple import *
from initiator_set.util.mRNA import mRNA
from initiator_set.kozak_calculator import kozak_loader
from initiator_set.kozak_calculator import kozak_consensus
from initiator_set.kozak_calculator import kozak_calculator


# Test for weak initiator AUC followed by stronger initiator GUC
with open("../map_aic/example_input_3.txt") as inf:
    with open("../kozak_calculator/sample_kozaks_3.txt") as ate:
        a = interpret_aic_weights(inf)
        print(a)
        b = mRNA("CCCAUCCCCGUCCCC")
        map_aic(b, a)

        c = kozak_loader.interpret_kozak_file(ate)

        kozak_runner = kozak_calculator.calculate_kozaks(b, c)


        print(b.code)
        print(b.metadata.__str__().replace('}, \'', '}, \n\''))

        print(is_leaky(b))


# Test for stronger initiator GUC followed by weaker initiator AUC
with open("../map_aic/example_input_3.txt") as inf:
    with open("../kozak_calculator/sample_kozaks_3.txt") as ate:
        a = interpret_aic_weights(inf)
        print(a)
        b = mRNA("CCCGUCCCCAUCCCC")
        map_aic(b, a)

        c = kozak_loader.interpret_kozak_file(ate)

        kozak_runner = kozak_calculator.calculate_kozaks(b, c)


        print(b.code)
        print(b.metadata.__str__().replace('}, \'', '}, \n\''))

        print(is_leaky(b))

