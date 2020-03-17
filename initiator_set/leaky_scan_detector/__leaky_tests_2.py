from initiator_set.util import mRNA
from initiator_set.leaky_scan_detector.leaky_scan_detector import *

# Tests STOP detection and lengths of sequence starting from any codon
mrna: mRNA = mRNA("AAAUUA")

calculate_lengths(mrna)

print(mrna.metadata)

mrna: mRNA = mRNA("UUAAAAGGGCCCUUA")

calculate_lengths(mrna)

print(mrna.metadata)

mrna: mRNA = mRNA("AAAAAUUAUUUAGGGGGG")

calculate_lengths(mrna)

print(mrna.metadata)

mrna: mRNA = mRNA("AAAAAUUAUUUAGGGGGGAAAAAUUAUUUAGGGGGG")

calculate_lengths(mrna)

print(mrna.metadata)
print(is_overlap(mrna, 8, 9))
print(is_overlap(mrna, 1, 2))
print(is_overlap(mrna, 1, 9))
print(is_overlap(mrna, 1, 3))
print(is_overlap(mrna, 1, 4))
print(is_overlap(mrna, 1, 5))
print(is_overlap(mrna, 3, 1))
print(is_overlap(mrna, 4, 1))
print(is_overlap(mrna, 5, 1))

