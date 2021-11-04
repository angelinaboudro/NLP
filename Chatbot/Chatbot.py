"""
Name:           Angelina Boudro
Date:           November 1st, 2020
Class:          Human Language Technologies
"""



'''
This chatbot is named Vika. Vika provides information about webscraped information that is saved in the chatbot.txt file. 
This allows Vika the necessary knowledge along with nlp techniques to answer questions regarding special topics. 

'''


# import libraries - for testing make sure all libraries are included and there are no nltk certificate issues. 
# Certificate issues will throw flags but the program will run as usually.


import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings('ignore')

'''
Here we will get necessary information from the  Latent Dirichlet Allocation (LDA) using the Gensim. 
This will get estimation estimation from a training corpus and inference of topic distribution on new, unseen documents. 

'''

num_docs = 1
docs = []
with open('webscrape.txt', 'r') as f:
    doc_chat = f.read().lower()
    doc_chat = doc_chat.replace('\n',' ')
    docs.append(doc_chat)

for i in range(num_docs):
    print(docs[i][:80])  # First few characters from the text file webscrape.txt allows you to see the document lines.


'''
Need to install gensim as well. This allows us to create the LDA model.
'''
from gensim import models, corpora
from nltk import word_tokenize
from nltk.corpus import stopwords

NUM_TOPICS = 6
# number of topics we are looking for in this document.

# Preprocessing the text form the webscrape.txt
def preprocess(docs, stopwords):
    processed_docs = []
    for doc in docs:
        tokens = [t for t in word_tokenize(doc.lower()) if t not in stopwords
                  and t.isalpha()]
        processed_docs.append(tokens)
    return processed_docs

preprocessed_docs = preprocess(docs, stopwords.words('english'))
for i in range(num_docs):
    print(preprocessed_docs[i][:8])

# showing the use of words and the length of the dictionary.
dictionary = corpora.Dictionary(preprocessed_docs)
print('len of dictionary: ', len(dictionary))
corpus = [dictionary.doc2bow(tokens) for tokens in preprocessed_docs]
print(corpus[0][:5])
print(dictionary[4], dictionary[2], dictionary[1])

# Creating the LDA model
lda_model = models.LdaModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)
for i in range(NUM_TOPICS):
    top_words = [t[0] for t in lda_model.show_topic(i,10)]
    print("\nTopics", str(i), ':', top_words)

print("\n")


import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages

# unique dictionary that will keep our reponses.
myDict = {}
# keeps the i like statement for each user which can be used in reponce from the chatbot Vika.
userslikings = {}
nltk.download('punkt')
nltk.download('wordnet')
'''
make sure that you don't run into certificate issues with punkt and wordnet. 
if you do then please look at: https://stackoverflow.com/a/42890688/1167890, by @doctorBroctor

or run this code to disable certficate verification on macbook, and should work on windows as well. 

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
'''

# We are reading the webscrap file from last project to get data for Vika.
with open('webscrape.txt', 'r', encoding='utf8', errors='ignore') as theFile:
    itIt = theFile.read().lower()

# here we would do the tokenization
# and list the sentences
sentenCE = nltk.sent_tokenize(itIt)


def checkIt(dict, key):
    if key in dict.keys():  # checks for existing keys in dictionary.
        return True
    else:
        return False



# lemmer of the words, adn preprocessing the file.
lemmer = WordNetLemmatizer()

def lemmmit(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

changePunct = dict((ord(punct), None) for punct in string.punctuation) #changing punctuation for use.

# normalizing it
def normalize(text):
    return lemmmit(nltk.word_tokenize(text.lower().translate(changePunct)))

# common greetings added.
commongreetings = (
"Zdravstvuyte", "sup", "what's up", "hey", "Hello", "How are you?")


# Interaction with the user.
def sayingHIIt(inputt):
    for word in inputt.split():
        if word.lower() in commongreetings:
            return "hi dude"

def responseToUser(OurInt
                   , name): #creates response to the user.
    introduce = OurInt

    botAnswer = ''
    if ("i'm" in OurInt
            or "i am" in OurInt
            or "my name is" in OurInt
            or "My name is" in OurInt
    ):
        if "i am" in OurInt\
                :
            OurInt\
                = OurInt\
                .replace("i am ", isname + " you are ")
        elif "i\'m" in OurInt\
                :
            OurInt\
                = OurInt\
                .replace("i\'m ", isname + " you are ")
        else:
            OurInt\
                = "you\'ve once before thought about " + OurInt

    if OurInt\
            not in myDict[name]:
        myDict[name].append(OurInt
                            )

    print(myDict[name])
    TfidfVec = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(myDict[name])

    # finding the similarty values here
    vals = cosine_similarity(tfidf[-1], tfidf)
    vals

    idx = vals.argsort()[0][-2]

#rouding the number
    round = vals.flatten()
    round.sort()

    req_tfidf = round[-2]

    # if the sentence said doesn't match anything
    if (req_tfidf == 0):
        botAnswer = botAnswer + "I didn\'t get what you just said"
        return botAnswer
    else:
        botAnswer = botAnswer + myDict[name][idx]
        return botAnswer


indicator = True
print(
    "Vika: My name is Vika. I want to get to know you, and give you some information about subjects. "
    "If you want to exit, type \"Exit\"!")

# this is where the user talks to it
while (indicator == True):

    print("Can you tell me your name please (NAME)")
    isname = input()
    isname = isname.lower()

    # checking if user exists
    if not checkIt(myDict, isname):
        myDict[isname] = []
        myDict[isname] = myDict[isname] + (sentenCE)

    print("Nice to meet you " + isname)

    # interact with user
    if (checkIt(userslikings, isname)):
        print(userslikings[isname][0])

    # learning things about the user
    print("Tell me something about yourself " + isname + "!")
    print("What do you like to do? (You can just write the word!)")
    UserInput = input()
    UserInput = UserInput.lower()

    # parsing user's input
    if ("i'm" in UserInput or "i am" in UserInput or "my name is" in UserInput or "My name is" in UserInput
            or "i like" in UserInput):
        if "i am" in UserInput:
            UserInput = UserInput.replace("i am ", isname + " you are ")
        elif "i\'m" in UserInput:
            UserInput = UserInput.replace("i\'m ", isname + " you are ")
        elif "i like" in UserInput:
            UserInput = UserInput.replace("i like ", isname + " you like ")
            if not checkIt(userslikings, isname):
                userslikings[isname] = []
                userslikings[isname].append(UserInput)
            else:
                userslikings[isname].append(UserInput)

        else:
            UserInput = "you are " + UserInput

    print("Magnificent! I like " + isname + " as much as you like " + UserInput + "!")
    myDict[isname].append(UserInput)

    print("what would you like to learn about? " + isname)
    OurInt\
        = input()
    OurInt\
        = OurInt\
        .lower()
    if (OurInt
            != 'Exit'):
        if (OurInt
                == 'you are goat' or OurInt
                == 'I love you'):
            indicator = False
            print("Vika: I love you too " + isname + "!")
        else:
            if (sayingHIIt(OurInt) != None):
                print("Vika: " + sayingHIIt(OurInt
                                              ))
            else:
                print("Vika: ", end="")
                print(responseToUser(OurInt
                                     , isname))

    else:
        indicator = False
        print("Vika: I\'m leaving I hate you.")


    myDict[isname].append(UserInput)

    print("What else would you like to know " + isname+ "?")
    OurInt\
        = input()
    OurInt\
        = OurInt\
        .lower()
    if (OurInt
            != 'Exit'): # you can leave the chat by typing exit
        if (OurInt
                == 'you are goat' or OurInt
                == 'I love you'):
            indicator = False
            print("Vika: I love you too " + isname + "!")
        else:
            if (sayingHIIt(OurInt) != None):
                print("Vika: " + sayingHIIt(OurInt))
            else:
                print("Vika: ", end="")
                print(responseToUser(OurInt, isname))

    else:
        indicator = False
        print("Vika: I\'m leaving I hate you.")


"""
Name:           Angelina Boudro
Date:           November 1st, 2020
Class:          Human Language Technologies
"""
