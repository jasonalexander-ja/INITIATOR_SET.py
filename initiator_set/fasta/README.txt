> Program: GUESS
> Module: Initiator Set
> Submodule: Fasta
> Author: Jordan Eckhoff
> e-mail: jeckhoff@vulpinedesigns.com

To use: run IS_Main.py, and when prompted select a .fa FASTA file. I used sample.fa when writing this code, but feel free to test it with any .fa FASTA file you want. 

This submodule will return the metadata and letter code as strings in a single FASTA_Raw_Seq object (or a list of them if there are multiple sequences) for each sequence in the FASTA file.

In the IS_Fasta_Sequence file, the Sequence_Translate function takes DNA sequences and translates them to mRNA, then to Protein sequences. It can also start or stop in the middle at mRNA if desired (see the comments in the function itself)

If a .fa file is selected that causes errors or a crash (that hasn't been purposely altered from the standard .fa format), please send the author an email with the file you used attached so the bug can be properly investigated.