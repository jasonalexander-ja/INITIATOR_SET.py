from initiator_set.kozak_calculator.kozak_consensus import *

# Various tests on KzConsensus

# This is why you want to use kozak_loader.py instead of directly instantiating KzConsensus instances
#                                   AAUGUC[G|C]
c21: KzConsensus = new_KzConsensus(1, (1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0,0.5,0.5))
print(str(c21))
print(str(c21.codon()))
print(c21.similarity_distribution("aaugucg"))
print(c21.similarity("aaugucg"))
print(c21.similarity_distribution("aaugucc"))
print(c21.similarity("aaugucc"))
print(c21.similarity_distribution("aaugugg"))
print(c21.similarity("aaugugg"))
print(c21.similarity_distribution("aauguga"))
print(c21.similarity("aauguga"))
print(c21.similarity_distribution("auuguga"))
print(c21.similarity("auuguga"))
print()

#                                   AAUGUCC
c21: KzConsensus = new_KzConsensus(1, (1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0,0,1))
print(str(c21))
print(c21.similarity_distribution("aaugucg"))
print(c21.similarity("aaugucg"))
print(c21.similarity_distribution("aaugucc"))
print(c21.similarity("aaugucc"))
print(c21.similarity_distribution("aaugugg"))
print(c21.similarity("aaugugg"))
print(c21.similarity_distribution("aauguga"))
print(c21.similarity("aauguga"))
print()

#                                   AAUGUC[U|G|C]
c21: KzConsensus = new_KzConsensus(1, (1,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1),(0,0.33,0.33,0.33))
print(str(c21))
print(c21.similarity_distribution("aaugucg"))
print(c21.similarity("aaugucg"))
print(c21.similarity_distribution("aaugucc"))
print(c21.similarity("aaugucc"))
print(c21.similarity_distribution("aaugugg"))
print(c21.similarity("aaugugg"))
print(c21.similarity_distribution("aauguga"))
print(c21.similarity("aauguga"))
print()
