def PERM(n,output_file):
    permutations_list =[]
    
    def permute_helper(current_perm,current_pos):
        if current_pos == len(current_perm):
            permutations_list.append(list(current_perm))
        else:
            for i in range(current_pos,len(current_perm)):
                current_perm[current_pos], current_perm[i] = current_perm[i], current_perm[current_pos]
                permute_helper(current_perm, current_pos + 1)
                current_perm[current_pos], current_perm[i] = current_perm[i], current_perm[current_pos]
    permute_helper(list(range(1, n+1)),0)
    
    with open(output_file,'w') as file:
        file.write(f"{len(permutations_list)}\n")
        for permutation in permutations_list:
            file.write(" ".join(map(str,permutation)) + "\n")

n = 6
output_file = "output3.txt"
PERM(n,output_file)