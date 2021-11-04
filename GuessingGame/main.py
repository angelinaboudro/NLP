"""
Name:           Angelina Boudro
Class:          Human Language Technologies
"""

import random
import nltk
nltk.download('punkt')
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag

def printList(listIn):
    for c in listIn:
        print(c, end=' ')


def compareListEqual(my_list, chosen_word):
    for i in range(len(my_list)):
        if my_list[i] != chosen_word[i]:
            return False


    return True

#STEP 1
def main():
    fileName = 'anat19.txt'
    try:
        with open(fileName) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            words = []
            for record in content:
                records = record.split(" ");
                for word in records:
                    words.append(word.strip())
    except:
        print("Error in opening file")
        return
#STEP 2
    file = open("anat19.txt").read()

    tokens = nltk.word_tokenize(file)
    num = len(set(tokens))/len(tokens)
    print("\nThe lexical diversity is {:0.2f}".format(num)) #******

#STEP 3
    #lower_case=fileName.lower()
    #stopwords('english')
    #SETP 3.A
    tokens = [t.lower() for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t)>5]

    #STEP 3.B
    WNL = WordNetLemmatizer()
    lemmas = (WNL.lemmatize(t) for t in tokens)
    unique = list (set(lemmas))
    print("The number for unique lemmas are: ", len(unique))

    #STEP 3.C
    tags = nltk.pos_tag(unique)
    print("The 20 tags are:", tags[:20])

    #STEP 3.D
    import re
    nouns = [lis for lis in tags if re.search('NN.*', lis[1])]
    #print("\nNumber of nouns is: ", len(nouns))
    #print(nouns)
    #print("Number of tokens is: ", tokens)
    #count = Counter(tag for word, tag in tags)
    #print("\nThe number of nouns is: ", count)

    #STEP 3.E
    print("Number of tokens is: ", len(tokens))
    print("Number of nouns is: ", len(nouns))

    #STEP 3 F will be included at the end of the program

    #STEP 4
    noun = {n:tokens.count(n) for n in tokens}
    nounDict = {}

    for n in noun:
        nounDict[n] = nouns.count(n)

    nounsSort = sorted(nounDict, key=nounDict.get, reverse=True)
    wordPool = nounsSort[:50]
    print("\nThis is the pool of 50 nouns and their occurrences that were randomly selected:", nounDict)

    #Guessing Game
    chance = 10
    print("\nYou will have", chance, " chances to guess all of the letters. Good luck!")

    chosen_word = random.choice(wordPool)
    print("Shown for purposes to prove random selection. The word to guess is:", chosen_word)

    round = 0
    totalGuess = 0
    gameOver = False
    while True:
        my_list = []
        round += 1
        print("ROUND ", round)
        for i in range(len(chosen_word)):
            my_list.append("_")
        print("The answer so far is ", end = "")
        printList(my_list)

        found = False;
        for i in range(chance):
            user_input = input("\nGuess a letter: ").lower()
            if user_input[0] == '!':
                gameOver = True
                break
            foundCurrent = False
            for k in range(len(chosen_word)):
                if user_input == chosen_word[k]:
                    foundCurrent = True
                    my_list[k] = chosen_word[k]
            if foundCurrent:
                print("Right!")
            else:
                 print("Sorry!! Guess Again")

            print("The answer so far is ", end="")
            printList(my_list)
            if compareListEqual(my_list, chosen_word):
                print('\nGood job! You found the word ' + chosen_word + ".")
                found = True;
                totalGuess += 1
                break

        if not found:
            print("\nNot quite, the correct word was " + chosen_word + ". Better luck next time!")
        if gameOver:
            break
    print("Total rounds played", round)
    print("Correct guesses", totalGuess)
    return tokens, nouns
main()

