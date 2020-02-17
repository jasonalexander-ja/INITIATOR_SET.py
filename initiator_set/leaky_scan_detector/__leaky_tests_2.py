from initiator_set.util.mRNA import *
from initiator_set.leaky_scan_detector.leaky_scan_detector import *

# first bleeds into second
mrna: mRNA = mRNA("AAAGGGUUUCCC")
mrna.metadata['locations_aic_chronological'] = [0, 6]
mrna.metadata['sequence_lengths'] = [9, 3]


print(detect_overlap(mrna))


# no bleeding
mrna.metadata['locations_aic_chronological'] = [0, 6]
mrna.metadata['sequence_lengths'] = [6, 3]
print(detect_overlap(mrna))