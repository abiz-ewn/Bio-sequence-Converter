"""
Program Name: DNA Translation to proteins
Author Name: Abigail Ewnetu
Program Description: This code translates DNA to mRNA, then converts mRNA to proteins.
"""
import helper

def transcription(dna_sequence):  # Function to transcribe DNA to mRNA
    mRNA = ""  # Empty string to define the variable mRNA for the following argument
    for pair in dna_sequence:
        if pair == "A":  # if pair is "A" then it will change it to "U" for mRNA
            mRNA += "U"
        elif pair == "T":  
            mRNA += "A"
        elif pair == "C":  
            mRNA += "G"
        elif pair == "G":  
            mRNA += "C"
    return mRNA


def translation(rna_sequence):  # defined a function that translates RNA sequence to proteins or amino acids
    triplets = helper.chunk(rna_sequence, 3)  # This variable splits RNA sequences to triplets imported from helper file
    protein_sequence = []  # Empty list for protein sequence
    
    for triplet in triplets:
        if triplet in helper.amino_acids:  # if triplet exists in the helper file, amino_acids dictionary
            amino_acid = helper.amino_acids[triplet]  # goes to the helper file, amino_acids dictionary to run the value of the key
            
            if amino_acid == "Stop":  
                print("Stop")
                break  
            
            protein_sequence.append(amino_acid)  # This code will add amino_acids to the protein sequence defined above
        else:
            print(f"Warning: Triplet {triplet} not found in amino acids dictionary.")
    

    return " ".join(protein_sequence) # returns the loop by joining protein sequences together


# This is the given DNA sequence being testing
dna_sequence = "TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT"
print("DNA Sequence:", dna_sequence)

# To convert DNA to mRNA
rna_sequence = transcription(dna_sequence)
print("mRNA Sequence:", rna_sequence)

#  To translate RNA to Protein sequence
protein_sequence = translation(rna_sequence)
print("Protein Sequence:", protein_sequence)
