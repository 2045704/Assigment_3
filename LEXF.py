from itertools import product

def LEXF(alphabet, n):
    comb = map(''.join, product(alphabet, repeat = n))
    result = sorted(comb)
    return result

with open(r"C:\Users\newma\Downloads\rosalind_lexf (1).txt","r") as file:
    alphabet = file.readline().strip().split()
    n = int(file.readline().strip())
    
result = LEXF(alphabet, n)

with open(r"3my_output.txt","w") as file2:
    for char in result:
        file2.write(f"{char}\n")