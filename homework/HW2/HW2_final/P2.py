# Problem 2 DNA Complement for Homework 2 of CS107
# Author: Max Li

def dna_complement(original):
    '''This function takes in a DNA sequence represented as a string and returns it complement as a string.'''
    bases = ['A', 'T', 'G', 'C']
    
    if len(original) == 0:
        return None
    for x in original:
        if x.upper() not in bases:
            return None
        
    complement = ''
    for x in original:
        if x.upper() == 'A':
            complement+='T'
        elif x.upper() == 'T':
            complement+='A'
        elif x.upper() == 'C':
            complement+='G'                   
        elif x.upper() == 'G':
            complement+='C'        
            
    return complement


example_1 = 'AatGGc'
example_2 = 'AATdog'
print('example 1: '+ example_1 + " has complement: ")
print(dna_complement(example_1))
print('example 2: '+ example_2 + " has complement: ")
print(dna_complement(example_2))