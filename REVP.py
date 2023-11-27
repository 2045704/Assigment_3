from Bio import SeqIO
from Bio.Seq import Seq

def REVP(input_file):
    record = SeqIO.read(input_file,"fasta")
    dna_seq = str(record.seq)
    
    results = []
    for i in range(len(dna_seq)):
        for j in range(4,13):
            if i + j <= len(dna_seq):
                substring = dna_seq[i:i+j]
                revc = str(Seq(substring).reverse_complement())
                if substring == revc:
                    results.append((i +1, j))
    return results

with open(r"C:\Users\newma\Downloads\rosalind_revp (1).txt","r") as file:
    results = REVP(file)

with open("3sample_output.txt", "w") as file2:
    for result in results:
        file2.write(f"{result[0]} {result[1]} \n")