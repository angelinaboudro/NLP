"""
Name:           Angelina Boudro
Class:          Human Language Technologies
"""

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer() # porter stemmer initializing
f = open("moby_dick.txt")  # opening the file
text = f.read()  # reading the file
f.close()  # closing the file

text = text.lower()
text = text.replace('--', '')
text = re.sub("\d+", "", text)
text_copy = text
text = re.sub(r'''[,.@#?!&$'"()]+''', "", text)
tokens = nltk.word_tokenize(text)
print("The number of tokens is:", len(tokens))
unique_set = set(tokens)
print("The number of unique tokens is: ", len(unique_set))
important_words = [word for word in unique_set if not word in stopwords.words()]
print("The number of important words is: ", len(important_words))

# Using the list we created of important words we will now create a list
# of tuples of the word and stemmed word.
important_stemmed_word = []
for word in important_words:
    important_stemmed_word.append((word, ps.stem(word)))
print("A list of tuples of the word and stemmed word: ", important_stemmed_word)

# Create a dictionary where the key is the stem, and the value is a list
# of words with that stem

stem_dict = {}
for word in important_stemmed_word:
    if word[1] in stem_dict:
        if word[0] not in stem_dict[word[1]]:
            stem_dict[word[1]].append(str(word[0]))
    else:
        stem_dict[word[1]] = [word[0]]
print("Length of the stem words dictionary is: ", len(stem_dict))  # printing the length of the dict

# 25 dictionary entries
count = 0
print('The longest list : in the form (stem : [list of words])')
for k in sorted(stem_dict, key=lambda k: len(stem_dict[k]), reverse=True):
    if count != 25:
        print(k, "\t: \t", stem_dict[k])
        count += 1


# Levenshtein Distance

def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for word in range(n + 1)] for word in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


# Driver program
str1 = 'continue'
str2 = stem_dict['continu']
    if count =

print(editDistDP(str1, str2, len(str1), len(str2)))


# POS tagging on the original text
tagged = nltk.pos_tag(text_copy.split())
# tagged
pos_count = {}
for word in tagged:
    if word[1] in pos_count:
        pos_count[word[1]] += 1
    else:
        pos_count[word[1]] = 1
print("The dictionary with POS count: \n", pos_count)
