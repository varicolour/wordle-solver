#wordle-solver
import random

# colours for prettier text
green = "\033[32m"
yellow = "\033[33m"
bold = "\033[1m"
clear = "\033[0m"

# open wordfile and put all the words into a list
wordfile = open("path/to/your/wordfile", "r")
wordList = []
loop = True
while loop == True:
    word = wordfile.readline()
    if word == "":
        loop = False
    else:
        wordList.append(word.strip())
wordfile.close()

guessesList = []
feedback = ""
blacklist = []
yellowlist = {}
greenlist = {}

while feedback != "done":
    check = False

    guess = random.randint(0, len(wordList) - 1)    # guess a random word
    guessedWord = wordList[guess]                   # store it for later

    # take the green and yellow lists (which are dicts) and put their keys and values in a list for later use
    greenKeys = list(greenlist.keys())
    greenValues = list(greenlist.values())

    yellowKeys = list(yellowlist.keys())
    yellowValues = list(yellowlist.values())

    if guess in guessesList:    #check if a word has already been guessed
        continue

    for _ in range(0, len(guessedWord)):    # check if a letter in the word is in the blacklist
        if guessedWord[_] in blacklist:
            check = True

    for i in range(0, len(greenKeys)):                  # check if a letter is in the greenlist and in the right place
        if guessedWord[greenKeys[i]] != greenValues[i]:
            check = True

    for c in range(0, len(yellowKeys)):                # check if a letter is in the yellowlist but in a different place
        if guessedWord[yellowKeys[c]] == yellowValues[c] or yellowValues[c] not in guessedWord:
            check = True
    
    if check == True:           # if any of the previous checks failed, make another guess
        print(guessedWord)      # and print the wrong guess (originally for debug but I liked how it looks)
        continue

    print(bold + green + guessedWord + clear)
    guessesList.append(guess)
    feedback = input(f"{bold}{yellow}feedback: {clear}")    # print guess that meets all the requirements and ask feedback

    if feedback != "done":
        for x in range(0, len(feedback)):
            if feedback[x] == "b":
                blacklist.append(guessedWord[x])
            if feedback[x] == "y":
                yellowlist.update({x: guessedWord[x]})
            if feedback[x] == "g":
                greenlist.update({x: guessedWord[x]})       # evaluate feedback and add corresponding letters to the lists specified in the feedback

    greenKeys = list(greenlist.keys())
    greenValues = list(greenlist.values())      # update greenlist keys and value lists

    for y in range(0, len(greenKeys)):              # if a letter is in both the blacklist and greenlist, remove it from blacklist and add it to yellowlist to prevent it from looping forever
        if greenlist[greenKeys[y]] in blacklist:    # !!! this part is not working properly yet !!!
            if greenKeys[y] < 5:
                yellowlistKey = greenKeys[y] + 1
            else:
                yellowlistKey = greenKeys[y] - 1
            yellowlist.update({yellowlistKey: greenlist[greenKeys[y]]})
            blacklist.remove(greenlist[greenKeys[y]])