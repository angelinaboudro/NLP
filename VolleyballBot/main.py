"""
Name: Angelina B
Class: Human Language Technologies
"""


import io
import os
import random
import string
import warnings
import numpy as np
from nltk import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import nltk
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)  # for downloading packages

# uncomment these only the first time you run it
# nltk.download('punkt')
# nltk.download('wordnet')

wnl = WordNetLemmatizer()


# removing punctuation
remove_punct = dict((ord(punct), None) for punct in string.punctuation)


# get the lemmas of a list of words
def get_lems(pre_words):
    return [wnl.lemmatize(token) for token in pre_words]


# preprocessing lemmas
def process_lems(text):
    return get_lems(nltk.word_tokenize(text.lower().translate(remove_punct)))


# keyword matching for greetings
greetings = ("hello", "hi", "hey",)
greeting_responses = ["Hi!", "Hey!", "Hi there!", "Hello!", "Howdy, partner.", "Hello, comrades."]

# dict of definitions, can all be used to provide random definition to user.
def_dict = {
    'ace': 'an ace is when a serve results directly in a point.',
    'assist': 'an assist is when a player helps a teammate set up for a kill.',
    'attacker': 'an attacker is a player who attempts to hit a ball offensively with the purpose of terminating play.',
    'back set': 'a back set is when a set is delivered behind the setter.',
    'baseline': 'the baseline is the back boundary of the court. Also called the end line.',
    'block': 'a block is meant to intercept a spiked ball.',
    'center line': 'the center line is the boundary that runs under the net and divides the court into two equal halves.',
    'deep': 'deep is referring to sending the ball into the far back of the opponents court.',
    'dig': 'a dig is how a player passes a spike or a a ball hit low to the ground.',
    'floater': 'a floater is a serve with no spin so the ball follows an erratic path.',
    'free ball': 'a free ball is a ball returned to the opponents without the intent to kill.',
    'held ball': 'a held ball is a ball that comes to rest during contact resulting in a violation.',
    'hit': 'a hit is to jump and strike the ball with an overhand, forcefful shot.',
    'hitter': 'a hitter is the player who is responsible for hitting the ball.',
    'joust': 'a joust is when 2 opposing players contact the ball simultaneouslyabove the net causing the ball to momenta'
            'rily come to rest. The point is then replayed.',
    'jump serve': 'a jump serve is when a server uses an approach, toss, takeoff and serves the ball with a spiking motion.',
    'kill': 'a kill is when an attack results directly in a point or sideout.',
    'libero': 'a libero is a player specialized in defensive skills.',
    'linesman': 'a linesman is an official located at the corners of the court, responsible for ruling if a ball is in or out.',
    'overhand pass': 'an overhand pass is a pass with both hands open that is controlled by the fingers',
    'overpass': 'an overpass is a ball passed across the net.',
    'pass': 'a pass is when a player makes contact with the ball with the intent to send the ball to another player',
    'red card': 'a red card is given by the official to a player for flagrant misconduct.',
    'rotation': 'the rotation is the clockwise movement of players around the court.',
    'serve': 'the serve is used to put the ball into play.',
    'set': 'the set it when the ball is directed to a point where a player can spike it into the opponents court.',
    'shank': 'a shank is a severely misdirected pass',
    'spike': 'a spike is when a ball is contacted with force by a player with the intent to terminate it on the other court.',
    'switch': 'a switch is to change court positions after a ball is served.',
    'tip': 'a tip a one-handed, soft hit into the opponents court using fingertips.',
    'touch': 'a touch is when a player contacts the ball on an offensive play.',
    'underhand serve': 'an underhand serve is one performed with an underhand striking action.',
    'yellow card': 'a yellow card is given by the official to a player as a warning of misconduct'
}

positives = ['yes', 'yeah', 'yup', 'sure', 'uh huh', 'yuppers', 'absolutely', 'yas']


# return a random greeting response when greeting is input by user
def greeting(sent):
    lower_text = sent.lower()
    for word in lower_text.split():
        if word in greetings:
            return random.choice(greeting_responses)


def get_level():
    """
    get's level of player
    :return: a string saying player level
    """
    # ask what level they played at
    level = input("What is the highest level you have played at? For example- High School, "
                  "College, Club, For Fun. ")
    level = level.lower()

    if 'pro' in level:
        stri2 = 'Level Played: Professional'
        print('Wow! Congratulations!')
    elif 'college' in level:
        stri2 = 'Level Played: College'
        print('Wow! Congratulations!')
    elif 'club' in level:
        stri2 = 'Level Played: Club'
    elif 'high school' in level or 'highschool' in level:
        stri2 = 'Level Played: High School'
    elif 'middle school' in level or 'middleschool' in level:
        stri2 = 'Level Played: Middle School'
    elif 'fun' in level:
        stri2 = 'Level Played: Fun'
        print('Dude, me too. I''m a computer, so it''s sort of difficult to break into competitive volleyball.')
    else:
        stri2 = 'Level Played: N/A'
        print('Wasn''t able to catch that, but that''s okay! It isn''t crucial to the rest of the experience.')

    return stri2


def get_posi():
    """
    Get's position of player
    :return: string of player position
    """
    # ask what position they play.
    position = input("What position did you play? ")
    position = position.lower()
    if len(position.split()) == 1:
        stri = 'Position: ' + position
    elif position.startswith('i played ') or position.startswith('i was '):
        stri = 'Position:', position.split()[2:]
    else:  # heck if I know what's happening
        print('I didn''t quite get that but I will save it to your file')
        stri = 'Position: (User response) ' + position

    return stri


def get_exp():
    """
    returns level of expertise of player
    :return: string of level of expertise and number of expertise
    """
    level = input("On a scale of 1-3, with 3 being expert, how much would you say you know about volleyball? ")
    level = level.lower()
    threes = ['3', 'three', 'tree', 'tres']
    twos = ['twos', 'two', 'to', '2']

    if any(x in level for x in threes):
        stri = 'Level = Expert'
        num_level = 3
        print('Excellent, I have identified you as an expert.')
        print('I will try to provide you with more advanced answers.')
    elif any(x in level for x in twos):
        stri = 'Level = Intermediate'
        num_level = 2
        print('Excellent, I have identified you as an intermediate.')
        print('I will try to provide you with mid-level answers.')
    else:  # if we can't identify what they are, we should mark them as beginner
        stri = 'Level = Beginner'
        num_level = 1
        print('Excellent, I have identified you as an beginner.')
        print('I will try to provide you with more detailed answers.')

    return stri, num_level


# used to gather some info on new users
def find_new_info():
    user_answers = []

    # initializing punctuations string
    punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''

    print("Since you're new, let's get to know each other a bit!")
    ans = input("Have you ever played volleyball? ")
    ans = ans.lower()

    # Removing punctuations in string
    # Using loop + punctuation string
    for ele in ans:
        if ele in punc:
            ans = ans.replace(ele, "")

    if any(x in ans for x in positives):
        stri1 = 'Status: Player'
        stri2 = 'Status: Not Player'
    else:
        stri1 = 'Status: Not Player'
        stri2 = 'Status: Player'

    check = input('I have identified you as ' + stri1 + '. Is this correct? (Y/N)')
    check = check.lower()

    if check == 'y' or any(x in check for x in positives):
        # do nothing
        user_answers.append(stri1)
    else:
        stri1 = stri2
        user_answers.append(stri1)

    if 'Not' in stri1:  # user is not a player, follow up questions
        seen = input('Have you ever watched a game? ')
        seen = seen.lower()

        if any(x in seen for x in positives) or seen == 'i have':
            stri = 'Seen Game Before: Yes'
        else:
            stri = 'Seen Game Before: No'

        user_answers.append(stri)
    else:  # user is a player, followup questions
        # get level of play
        stri = get_level()
        user_answers.append(stri)

        # ask what position they play.
        stri = get_posi()
        user_answers.append(stri)

    # add to user answers, but at the front so it is easy to find
    stri, num_e = get_exp()
    user_answers.insert(0, stri)

    print('Excellent, enjoy chatting!')

    return user_answers, num_e


def get_response(user_inputs, sentences):

    chatbot_response = ''
    sentences.append(user_inputs)

    # use process_lems as our tokenizer and english stop words
    vectorizer = TfidfVectorizer(tokenizer=process_lems, stop_words='english')

    # send all of our sentences into tfidf
    tfidf = vectorizer.fit_transform(sentences)

    # get cosine similarity values
    cos = cosine_similarity(tfidf[-1], tfidf)

    # sort the cosine similarity values
    sorted_cos = cos.argsort()[0][-2]

    # flatten sorted array
    flat = cos.flatten()
    # sort flattened array
    flat.sort()

    req_tfidf = flat[-2]

    # if chatbot doesn't recognize any key words
    if req_tfidf == 0:
        chatbot_response = chatbot_response + "I'm sorry, I don't understand what you're saying."
        return chatbot_response
    else:
        chatbot_response = chatbot_response + sentences[sorted_cos]
        return chatbot_response


if __name__ == '__main__':
    flag = True

    print("*** Welcome to a chat bot for Volleyball! We know, niche.***")
    print("***If you want to leave the chat, say goodbye or bye***")

    # chat bot greets user
    print(random.choice(greeting_responses))

    # prompt for name, and create user model from that
    user_name = input("What's your name? ")

    # search to see if user already exists in database
    # if user model already exists, append to file
    lower_name = user_name.lower()
    new_name = lower_name.replace(" ", "")
    # create outfile name
    outfile_name = "user_model_" + new_name + ".txt"

    if os.path.exists("user_model_" + new_name + ".txt"):
        print("I've see you've been here before! Welcome back, " + user_name + ".")
        # open file to read in the user level
        infile = io.open(outfile_name, 'r')

        # read in first line and discard, second and read
        infile.readline()  # discard this one
        level_finder = infile.readline()
        player_or_not = infile.readline()
        level_player_or_seen_game = infile.readline()

        # close file
        infile.close()

        if 'Expert' in level_finder:
            level = 3
        elif 'Intermediate' in level_finder:
            level = 2
        else:
            level = 1

        if 'Not' in player_or_not:
            if 'Yes' in level_player_or_seen_game:
                watched = input("Have you watched anymore volleyball since last time?")
                watched = watched.lower()

                if any(x in watched for x in positives):
                    print("Oh, awesome! Hope the team you were cheering for won!")
                else:
                    print("Ah, well maybe next time! There's nothing more fun than volleyball!")
            else:
                watched = input("Have you gotten the chance to watch a match yet?")
                watched = watched.lower()

                if any(x in watched for x in positives) or 'i have' in watched or 'i did' in watched and not 'not' in watched:
                    print("Oh, awesome! I have to watch all my volleyball on the internet, since I'm but a computer.")
                    print("I'll update your file.")
                    infile = io.open(outfile_name, 'r')
                    infile_old = infile.readlines()
                    infile.close()

                    outfile_new = []

                    for string in infile_old:
                        if 'Seen Game Before: No' in string:
                            new_string = 'Seen Game Before: Yes\n'
                        else:
                            new_string = string
                        outfile_new.append(new_string)

                    outfile = io.open(outfile_name, 'w')

                    for string in outfile_new:
                        outfile.write(string)

                    outfile.close()

                else:
                    print("Ah, well maybe by next time!")
        else:  # they are a player
            played = input("Have you gotten a chance to play any volleyball recently?")
            played = played.lower()

            if any(x in played for x in positives) or 'i have' in played and not 'not' in played:
                print("Ah, rocking! Wish I could play volleyball, but alas, I am but a computer.")
            else:
                print("Ah! Well maybe soon you will get the chance!")

        outfile = io.open(outfile_name, 'a')
    # if user model does not already exist
    else:
        print("Welcome, " + user_name + ". I'll create your user model now!")
        # create new text file/user model for user based off their name
        outfile = io.open(outfile_name, 'w', encoding="utf-8")
        # write user's name to file
        outfile.write(user_name + '\n')
        info_list, level = find_new_info()  # level is used to personalize what the user is seeing

        for fact in info_list:
            outfile.write(fact + '\n')

    # open knowledge base beginner
    with open('knowledge_base.txt', 'r', encoding='utf8', errors='ignore') as file:
        raw_knowledge_text = file.read().lower()

    # tokenize text
    knowledge_sentences = sent_tokenize(raw_knowledge_text)
    knowledge_words = word_tokenize(raw_knowledge_text)

    print("So, what can I help you with today?")

    while flag:
        # get user input and change it to lowercase
        user_input = input()
        user_input = user_input.lower()

        # if user chooses to leave chat
        if user_input == 'goodbye' or user_input == 'bye' or user_input == 'goodbye.' or user_input == 'bye.' \
                or user_input == 'goodbye!' or user_input == 'bye!':
            print("Goodbye!")
            flag = False
        # if user does not leave chat
        else:
            # if user says thanks, say your're welcome instead of searching for a response
            if user_input == 'thanks' or user_input == 'thank you' or user_input == 'thanks.' or \
                    user_input == 'thank you.' or user_input == 'thanks!' or user_input == 'thank you!':
                print("You're welcome!")
            elif 'thank' in user_input:
                print("You're welcome!")
            # otherwise, look for an appropriate response
            else:
                # if user says a greeting
                if greeting(user_input) is not None:
                    print(greeting(user_input))

                # if user says something about themselves
                elif 'i feel' in user_input or 'i like' in user_input:
                    # save it to the text file/user model
                    outfile.write(user_input + '\n')
                    print("That's awesome, thanks for sharing!")

                # if user asks a questions or wants a definition
                elif 'what is' in user_input or 'definition' in user_input or 'do you know what' in user_input or \
                        'if you know what' in user_input:
                    found_key = False
                    for key, value in def_dict.items():
                        if key in user_input:
                            print('From my understanding,', value)
                            found_key = True

                    if not found_key:
                        print(end="")
                        print(get_response(user_input, knowledge_sentences))
                        knowledge_sentences.remove(user_input)

                # otherwise, find appropriate response
                else:
                    print(end="")
                    print(get_response(user_input, knowledge_sentences))
                    knowledge_sentences.remove(user_input)

    outfile.close()