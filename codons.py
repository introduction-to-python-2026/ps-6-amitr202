def create_codon_dict(file_path):
   path = "data/codons.txt"
   file = open(path)
   rows = file.readlines()
   file.close ()

   my_dict = {}
   for row in rows:
    cells = row.strip().split('\t')
    codon = cells[0]
    aa_abrev = cells[2]
    my_dict.update({codon:aa_abrev}) 
   return my_dict  
