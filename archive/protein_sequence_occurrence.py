#protein_sequence_occurrence.py
#Author: Punit Sundar
#Purpose: Counts the #s of each amino acid in a given sequence

def get_aa_count(sequence):
    """Funtion returns a dictionary as well as a list of just the number\
of occurrences of each amino acid"""
    amino_acids = ["G","A","V","L","I","P","C","M","F","W","S",\
                   "T","Y","N","Q","K","R","H","D","E"]
    all_counts = {}
    for aminos in amino_acids:
        count = sequence.count(aminos)
        all_counts[aminos] = count
    list_occurrences = list(all_counts.values())
    return all_counts, list_occurrences

given_sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQR\
FFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVL\
AHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

#I separated the first returned output from the function in dictionary variable
dictionary = get_aa_count(given_sequence)[0]

#list_occurrences stores the 2nd part of the retun output from function 
list_occurrences = get_aa_count(given_sequence)[1]

#Reverse the list so the occurrences go from highest to smallest
list_occurrences.sort(reverse = True)

print(dictionary)
print(list_occurrences)

#sorted_list prints the amino acids from the most frequently occurring to the
#least frequently occurring amino acids
sorted_list = sorted(dictionary,key = dictionary.get,reverse=True)[::]
print(sorted_list)

#List of the chords for the most hydrophobic amino acids
hydrophobic_chords = ['A','B','C','D','E','F','G']  #these will be A through G chords with sine wave
                                                    #instrumentation from pyaudio aynthesizer
less_hydrophobic_chords = ['A','B','C','D','E','F','G']  #These will be single notes A through G
                                                        
part_hydrophobic_chords = ['R','K']  #these will be chords A through G but with sawtooth instrument
nonhydrophobic_chords = ['N','Q','D','E']  #these will be minor chords with sine wave instrumentation
'''
for amino in sorted_list[:7]:
    
    
'''   



#print(list_occurrences.sort(reverse = True))
    


##Very hydrophobic amino acids: V,I,L,M,F,W,C  
##Less hydrophobic amino acids: A,Y,H,T,S,P,G  
##Part hydrophobic amino acids: R,K  ##R is positively charged polar, #K is positively
                                                                      #charged polar

##N,Q,D,E not hydrophobic in the least
#N is polar
#Q is polar
#D is negatively charged polar
#E is negatively charged polar


