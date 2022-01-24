from repackage import up
up() # required to make python start searching modules from the parent directory
from util.mRNA import mRNA
from leaky_scan_detector.leaky_scan_detector import calculate_lengths
from leaky_scan_detector.leaky_scan_detector import is_overlap

# Tests STOP detection and lengths of sequence starting from any codon
mrna: mRNA = mRNA("AAAUUA")

calculate_lengths(mrna)

print(mrna.Metadata)

mrna: mRNA = mRNA("UUAAAAGGGCCCUUA")

calculate_lengths(mrna)

print(mrna.Metadata)

mrna: mRNA = mRNA("AAAAAUUAUUUAGGGGGG")

calculate_lengths(mrna)

print(mrna.Metadata)

mrna: mRNA = mRNA("AAAAAUUAUUUAGGGGGGAAAAAUUAUUUAGGGGGG")

calculate_lengths(mrna)

print(mrna.Metadata)
print(is_overlap(mrna, 8, 9))
print(is_overlap(mrna, 1, 2))
print(is_overlap(mrna, 1, 9))
print(is_overlap(mrna, 1, 3))
print(is_overlap(mrna, 1, 4))
print(is_overlap(mrna, 1, 5))
print(is_overlap(mrna, 3, 1))
print(is_overlap(mrna, 4, 1))
print(is_overlap(mrna, 5, 1))

