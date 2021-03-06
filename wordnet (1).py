# importing the library

import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet

# lets use word paint as an exqmple
syns = wordnet.synsets("paint")
# An example of a synset:
print(syns[0].name())
print('\n')
# Just the word:
print(syns[0].lemmas()[0].name())
print('\n')

# Definition of that first synset:
print(syns[0].definition())
print('\n')
# Examples of the word in use in sentences:
print(syns[0].examples())
print('\n')

from nltk.corpus import wordnet

syn = wordnet.synsets('good')[0]

print("Synset name :  ", syn.name())

print("\nHypernyms Synset abstract term :  ", syn.hypernyms())

print("\nHyponyms Synset specific term :  ",
      syn.hypernyms()[0].hyponyms())
syn.root_hypernyms()
print("\nSynset root hypernerm :  ", syn.root_hypernyms())
syn = wordnet.synsets('tree')[0]
print("\nSubstance Meronyms : ",syn.substance_meronyms())
print("\nPart Meronyms : ",syn.part_meronyms())
syn = wordnet.synsets('hydrogen')[0]
print("\nSubstance holonyms : ",syn.substance_holonyms())
syn = wordnet.synsets('atom')[0]
print("\nPart holonyms : ",syn.part_holonyms())
syn = wordnet.synsets('eat')[0]
print("\nEntailments : ",syn.entailments())

