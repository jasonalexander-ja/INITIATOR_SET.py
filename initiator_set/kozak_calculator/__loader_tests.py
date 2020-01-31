from typing import *

from initiator_set.kozak_calculator.kozak_calculator import *

from initiator_set.kozak_calculator.kozak_loader import interpret_kozak_file

with open("sample_kozaks.txt") as inf:
    a: List[KzConsensus] = interpret_kozak_file(inf, "sample_kozaks.txt")
    for x in a:
        print("Start codon of "+x.__repr__()+": "+x.codon())
    print(a.__repr__())
    print()
    print("gccgccaccaugg")
    print(a[0].similarity_distribution("gccgccaccaugg", 0))
    print(a[0].similarity("gccgccaccaugg", 0))
    print()
    print("aaagccgccaccaugg, starting from index 3")
    print(a[0].similarity_distribution("aaagccgccaccaugg", 3))
    print(a[0].similarity("aaagccgccaccaugg", 3))
    print()
    print("uuuuuuguuaugg")
    print(a[0].similarity_distribution("uuuuuuguuaugg", 0))
    print(a[0].similarity("uuuuuuguuaugg", 0))
    print()
    print("uuuuuuauuaugg")
    print(a[0].similarity_distribution("uuuuuuauuaugg", 0))
    print(a[0].similarity("uuuuuuauuaugg", 0))
    print()
    print("uuuuuuuuuaugu")
    print(a[0].similarity_distribution("uuuuuuuuuaugu", 0))
    print(a[0].similarity("uuuuuuuuuaugu", 0))
    print()
    print("uuuuuuuuuuuuu")
    print(a[0].similarity_distribution("uuuuuuuuuuuuu", 0))
    print(a[0].similarity("uuuuuuuuuuuuu", 0))
    print()
    print("uuuuuuuuuucuu")
    print(a[0].similarity_distribution("uuuuuuuuuucuu", 0))
    print(a[0].similarity("uuuuuuuuuucuu", 0))

with open("sample_kozaks_2.txt") as inf:
    a: List[KzConsensus] = interpret_kozak_file(inf, "sample_kozaks_2.txt")
    print(a.__repr__())
    print()
    print("cccaucccc -> cccaucccc")
    print(a[0].similarity_distribution("cccaucccc", 0))
    print(a[0].similarity("cccaucccc", 0))
    print()
    print("gggccc -> gggcc[c|g]")
    print(a[1].similarity_distribution("gggccc", 0))
    print(a[1].similarity("gggcca", 0))