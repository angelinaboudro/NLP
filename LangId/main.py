"""
Name:           Angelina Boudro
Class:          Human Language Technologies
"""

import nltk.corpus
import pickle
import fileinput

# Computing the English file
file = open(input("Enter English File:  'LangId.train: ")).read() # Open the English lang ID file as the naming convention says.

# PRe processing and clearning the white line.
for line in fileinput.FileInput("LangId.train.English", inplace=1):
    if line.rstrip():
        print(line)

# Creating tokens
English_unigram = nltk.word_tokenize(file)
English_bigrams = [(English_unigram[k], English_unigram[k+1]) for k in range (len(English_unigram)-1)] # Creating bigrams
English_unigram_dict = {t:English_unigram.count(t) for t in set(English_unigram)}

#Creating a pickle  Unigram
with open("English_unigram.pickle", "wb") as handle:
    pickle.dump(English_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("English_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

# Creating a dictionary of the tokens
English_bigram_dict = {b:English_bigrams.count(b) for b in set(English_bigrams)}

#PICKLE for the Bigram
with open("English_bigram.pickle", "wb") as handle:
    pickle.dump(English_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("English_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)

# French Language processing same as English and Italian
file = open(input("Enter French File:  'LangId.train: ")).read()
for line in fileinput.FileInput("LangId.train.French", inplace=1):
    if line.rstrip():
        print(line)

French_unigrams = nltk.word_tokenize(file)
French_bigrams = [(French_unigrams[k], French_unigrams[k+1]) for k in range (len(French_unigrams)-1)]
French_unigram_dict = {t:French_unigrams.count(t) for t in set(French_unigrams)}
#PICKLE
with open("French_unigram.pickle", "wb") as handle:
    pickle.dump(French_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("French_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

French_bigram_dict = {b:French_bigrams.count(b) for b in set(French_bigrams)}
#PICKLE
with open("French_bigram.pickle", "wb") as handle:
    pickle.dump(French_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("French_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)


#Italian
file = open(input("Enter Italian File:  'LangId.train: ")).read()

for line in fileinput.FileInput("LangId.train.Italian", inplace=1):
    if line.rstrip():
        print(line)

Italian_unigrams = nltk.word_tokenize(file)
Italian_bigrams = [(Italian_unigrams[k], Italian_unigrams[k+1]) for k in range (len(Italian_unigrams)-1)]
Italian_unigram_dict = {t:Italian_unigrams.count(t) for t in set(Italian_unigrams)}
#PICKLE
with open("Italian_unigram.pickle", "wb") as handle:
    pickle.dump(Italian_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("Italian_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

Italian_bigram_dict = {b:Italian_bigrams.count(b) for b in set(Italian_bigrams)}
#PICKLE
with open("Italian_bigram.pickle", "wb") as handle:
    pickle.dump(Italian_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("Italian_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)

''' 
Main.py will run and create the 6 dictionaries 3 unigram and 3 bigram for the 3 languages we have. 
then the comparion calc will give the lapalce of each of the language and use it to calcualte the accuracy
'''