from Bio import Phylo
import io

def CTBL(tree):
    def get_taxa(current_clade):
        taxa_set = set()
        for child_clade in current_clade.clades:
            taxa_set.update(get_taxa(child_clade))
        if current_clade.name:
            taxa_set.add(current_clade.name)
        current_clade.taxa_set = taxa_set
        return taxa_set
    
    def process_node(current_clade, all_taxa_labels):
        if len(current_clade.taxa_set) not in (0,1,total_taxa - 1, total_taxa):
            return ''.join(map(str, map(int, map(current_clade.taxa_set.__contains__, all_taxa_labels))))
        return None
    
    all_taxa_labels = sorted(get_taxa(tree.root))
    total_taxa = len(all_taxa_labels)
    
    return [process_node(clade,all_taxa_labels) for clade in tree.find_clades()]

with open(r"C:\Users\newma\Downloads\rosalind_ctbl (4).txt", "r") as input_file:
    newick_string = input_file.readline().strip()


phylogenetic_tree = Phylo.read(io.StringIO(newick_string), 'newick')

charachter_table = CTBL(phylogenetic_tree)

with open("3my_output.txt", "w") as output_file:
    for row in charachter_table:
        if row is not None:
            output_file.write(row + '\n')
