from initiator_set.map_aic_alternative.aic_weights_loader import *
from initiator_set.map_aic_alternative.map_aic import *

with open("example_input.txt") as inf:
    a = interpret_aic_weights(inf)
    print(a)
    b = mRNA("AUGGUGCUCCUGAUG")
    map_aic(b, a)

    print()



