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
