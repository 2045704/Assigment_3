from itertools import combinations, product

def EUBT(species_names):
    n = len(species_names)
    if n == 1:
        return [species_names[0]]
    
    all_trees = []
    global_species_set = set(species_names)

    for i in range(1, n // 2):
        subset_combinations = combinations(species_names, i)
        for subset in subset_combinations:
            all_trees += ['(' + x[0] + ',' + x[1] + ')' for x in product(
                EUBT(list(subset)),
                EUBT(list(global_species_set - set(subset)))
            )]

    if n % 2 == 0:
        subset_combinations = set(combinations(species_names, n // 2))
        used_subsets = set()

        for subset in subset_combinations:
            complementary_subset = frozenset(global_species_set - set(subset))

            if subset not in used_subsets and complementary_subset not in used_subsets:
                used_subsets |= set([frozenset(subset), complementary_subset])
                all_trees += ['(' + x[0] + ',' + x[1] + ')' for x in product(
                    EUBT(list(subset)),
                    EUBT(list(complementary_subset))
                )]

    else:
        subset_combinations = combinations(species_names, n // 2)
        for subset in subset_combinations:
            all_trees += ['(' + x[0] + ',' + x[1] + ')' for x in product(
                EUBT(list(subset)),
                EUBT(list(global_species_set - set(subset)))
            )]

    return all_trees

with open(r"C:\Users\newma\Downloads\rosalind_eubt (7).txt", 'r') as file:
    species_names = file.read().split()

all_unrooted_trees = EUBT(species_names[:-1])


with open("3my_output.txt", 'w') as output_file:
    for tree in all_unrooted_trees:
        output_file.write('(' + tree + ')' + species_names[-1] + ';\n')

