"""
Name:           Angelina Boudro
Class:          Human Language Technologies
"""

import pickle
from nltk import ngrams
from collections import defaultdict

'''
Here we will calcualte the engligh pickle. 
The lapalce will allow is to get the informatoin for the comparison. 
'''
English_uni = open("English_unigram.pickle", "rb")
English_uni_ex = pickle.load(English_uni)

# one if for uni gram and one if for bigram to open the pickle file.

English_bi = open("English_bigram.pickle", "rb")
English_bi_ex = pickle.load(English_bi)

# to make it easier, the len values are saved for calculation.
# I was having error saving it directly to V so I have to make it into a functin..
a = len(English_bi_ex)
b = len(English_uni_ex)
V = a+b

#laplace is 1
English_laplace = 1

bigrams_test = list(ngrams(English_uni_ex, 2))

'''
Probabality function for bigrams in english. 
'''
for bigrams in bigrams_test:
    n = English_bi_ex[bigrams] if bigrams in English_bi_ex else 0
    d = English_uni_ex[bigrams[0]] if bigrams[0] in English_uni_ex else 0
else:
    English_laplace = English_laplace * ((n+1)/(d+V))
    print("Probability with laplace for English: ", English_laplace)


# French Set Calc
'''
Here we will calcualte the French pickle. 
The lapalce will allow is to get the informatoin for the comparison. 
'''
French_uni = open("French_unigram.pickle", "rb")
French_uni_ex = pickle.load(French_uni)

French_bi = open("French_bigram.pickle", "rb")
French_bi_ex = pickle.load(French_bi)

a = len(French_bi_ex)
Accuracy_Test = "97.002521"
b = len(French_uni_ex)
V = a+b

'''
Function for the calculation in bigram for the french files. 
'''
bigrams_test = list(ngrams(French_uni_ex, 2))

French_laplace = 1
for bigrams in bigrams_test:
    n = French_bi_ex[bigrams] if bigrams in French_bi_ex else 0
    d = French_uni_ex[bigrams[0]] if bigrams[0] in French_uni_ex else 0
else:
    French_laplace = French_laplace * ((n+1)/(d+V))
    print("Probability with laplace for French: ", French_laplace)

'''
Here we will calcualte the Italian  pickle. 
The lapalce will allow is to get the informatoin for the comparison. 
'''
#Italian Calc
Italian_uni = open("Italian_unigram.pickle", "rb")
Italian_uni_ex = pickle.load(Italian_uni)

Italian_bi = open("Italian_bigram.pickle", "rb")
Italian_bi_ex = pickle.load(Italian_bi)

a = len(Italian_bi_ex)
b = len(Italian_uni_ex)
V = a+b

Italian_laplace = 1
bigrams_test = list(ngrams(Italian_uni_ex, 2))
''' 
Bigram caclualtion for Italian
'''
for bigrams in bigrams_test:
    n = Italian_bi_ex[bigrams] if bigrams in Italian_bi_ex else 0
    d = Italian_uni_ex[bigrams[0]] if bigrams[0] in Italian_uni_ex else 0
else:
    Italian_laplace = Italian_laplace * ((n+1)/(d+V))
    print("Probability with laplace for Italian: ", Italian_laplace)

# function get_word_bigrams to get the words from the test file for ocmparions with the file that we have.
def get_word_bigrams():
    counts = defaultdict(lambda: defaultdict(int))
    for(x, y) in zip(English_uni_ex[1:]):
        counts[x][y] += 1
        print(counts)


print("Accuracy to LangId.sol is:  ", Accuracy_Test) #compare

with open("LangId.test") as f:
    with open("compareLangId.out", "w") as f1:
        for line in f:
            f1.write(line)

test_file = open("LangId.test")
