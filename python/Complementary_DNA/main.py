# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the
# "instructions" for the development and functioning of living organisms.
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell);
# you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    ret_str = ''
    ret_str = (dna.replace('A', 'T') and dna.replace('T', 'A') and dna.replace('C', 'G') and dna.replace('G', 'C'))
    return ret_str

def DNA_strand_(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def _DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

print(_DNA_strand("ATC"))