from Bio import SeqIO

def KMP(s):
    j = -1
    b = [j]
    
    for el, x in enumerate(s):
        while j >= 0 and s[j] != x:
            j = b[j]
        j +=1
        b.append(j)
    
    return b[1:]


with open(r"C:\Users\newma\Downloads\rosalind_kmp (2).txt", "r") as file:
    record = SeqIO.read(file, "fasta")
    dna = str(record.seq)

result = KMP(dna)

with open("3my_output.txt", "w") as output_file:
    output_file.write(' '.join(map(str, result)))