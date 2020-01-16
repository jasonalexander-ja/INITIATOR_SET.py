from initiator_set.kozak_calculator.kozak_loader import interpret_kozak_file

with open("sample_kozaks.txt") as inf:
    a = interpret_kozak_file(inf)
    print(a.__repr__())