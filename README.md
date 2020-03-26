INITIATOR SET is a module of The GUESS intended to allow the calculation of the 
probabilities of Alternative Initiation Codons affecting the translation of mRNA
strands of nucleotides (A, G, C, U (RNA has U instead of the T seen in DNA. 
Artificial nucleotides may also be simulated here)) into proteins, and thus 
provide data for other modules handling protein folding and pathways. It is also 
intended for the origins of particular proteins to be possible to deduce in 
terms of mRNA sequences via calculating the AICs that would be present and thus 
the likelihood of mutations affecting particular proteins, and which genes need 
to be edited or epigenetically adjusted, for example. Its output data will also
have applications in tracking the causes of prion and amyloid diseases, and it 
can be used in working out which type of gene edit is safest to make where one 
has a choice and how mutations cause cancer.

INITIATOR SET will be based on the use of Intermine, a bioinformatic data 
aggregation platform from the University of Cambridge, along with whatever other
tools are required to fulfill all the steps of data handling outlined in the
diagram in this repository.

INITIATOR SET is intended to be the first of many modules to be developed for
The GUESS in such a way as will work standalone as well as connected to other 
modules.

- Danfox Davies


How to run:
1. Install pipenv
2. Open terminal at this location
3. pipenv install - installs some required packages automatically
4. pipenv shell - goes into a virtual python environment where the installed packages are available
5. python [runnable script]


