from typing import *

from initiator_set.kozak_calculator.kozak_calculator import *

from initiator_set.kozak_calculator.kozak_loader import interpret_kozak_file

with open("sample_kozaks.txt") as inf:
    a: List[KzConsensus] = interpret_kozak_file(inf)
    print(a.__repr__())
    print()
    print("gccgccaccaugg")
    print(a[0].confidence_distribution("gccgccaccaugg", 0))
    print(a[0].confidence("gccgccaccaugg", 0))
    print()
    print("aaagccgccaccaugg, starting from index 3")
    print(a[0].confidence_distribution("aaagccgccaccaugg", 3))
    print(a[0].confidence("aaagccgccaccaugg", 3))
    print()
    print("uuuuuuuuuaugu")
    print(a[0].confidence_distribution("uuuuuuuuuaugu", 0))
    print(a[0].confidence("uuuuuuuuuaugu", 0))
    print()
    print("uuuuuuuuuuuuu")
    print(a[0].confidence_distribution("uuuuuuuuuuuuu", 0))
    print(a[0].confidence("uuuuuuuuuuuuu", 0))
    print()
    print("uuuuuuuuuucuu")
    print(a[0].confidence_distribution("uuuuuuuuuucuu", 0))
    print(a[0].confidence("uuuuuuuuuucuu", 0))
