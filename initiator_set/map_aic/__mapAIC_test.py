from repackage import up
up()
from map_aic import mapAIC
from fasta import FastaSeq
from util import mRNA

mRNASequences = 'GCCGCCACCAUGGGCCGCCACCAUGGGCCGCCACCAUGCGCCGCCACGAUGGCUGAAA'
# '''CUGGCUCAGCGC'''
# GGGGGGGCGCGGAGACCGCGAG'''
# GCGACCGGGAGCGGCUGGGUUCCCGGCUGCGCGCCCUUCGGCCAGGCCGGGAGCCGCGCCAGUCGGAGCCCCCGGCCCAGCGUGGUCCGCCUCCCUCUGGGCGUCCACCUGCCCGGAGUACUGCCAGCGGGCAUGACCGACCCACCAGGGGCGCCGCCGCCGGCGCUCGCAGGCCGCGGAUGAAGAAGAAAACCCGGCGCCGCUCGACCCGGAGCGAGGAGUUGACCCGGAGCGAGGAGUUGACCCUGAGUGAGGAAGCGACCUGGAGUGAAGAGGCGACCCAGAGUGAGGAGGCGACCCAGGGCGAAGAGAUGAAUCGGAGCCAGGAGGUGACCCGGGACGAGGAGUCGACCCGGAGCGAGGAGGUGACCAGGGAGGAAAUGGCGGCAGCUGGGCUCACCGUGACUGUCACCCACAGCAAUGAGAAGCACGACCUUCAUGUUACCUCCCAGCAGGGCAGCAGUGAACCAGUUGUCCAAGACCUGGCCCAGGUUGUUGAAGAGGUCAUAGGGGUUCCACAGUCUUUUCAGAAACUCAUAUUUAAGGGAAAAUCUCUGAAGGAAAUGGAAACACCGUUGUCAGCACUUGGAAUACAAGAUGGUUGCCGGGUCAUGUUAAUUGGGAAAAAGAACAGUCCACAGGAAGAGGUUGAACUAAAGAAGUUGAAACAUUUGGAGAAGUCUGUGGAGAAGAUAGCUGACCAGCUGGAAGAGUUGAAUAAAGAGCUUACUGGAAUCCAGCAGGGUUUUCUGCCCAAGGAUUUGCAAGCUGAAGCUCUCUGCAAACUUGAUAGGAGAGUAAAAGCCACAAUAGAGCAGUUUAUGAAGAUCUUGGAGGAGAUUGACACACUGAUCCUGCCAGAAAAUUUCAAAGACAGUAGAUUGAAAAGGAAAGGCUUGGUAAAAAAGGUUCAGGCAUUCCUAGCCGAGUGUGACACAGUGGAGCAGAACAUCUGCCAGGAGACUGAGCGGCUGCAGUCUACAAACUUUGCCCUGGCCGAGUGA'''

mrna = mRNA.mRNA(mRNASequences)

mrna = mapAIC.mapAICs(mrna)

print('A is ' + str(mRNA.bases.index('A')))
print('U is ' + str(mRNA.bases.index('U')))
print('G is ' + str(mRNA.bases.index('G')))
print('C is ' + str(mRNA.bases.index('C')))
print(mrna.__str__())
