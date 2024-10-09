#wordle-solver
import random

green = "\033[32m"
yellow = "\033[33m"
bold = "\033[1m"
clear = "\033[0m"

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

    guess = random.randint(0, len(wordList) - 1)
    guessedWord = wordList[guess]

    greenKeys = list(greenlist.keys())
    greenValues = list(greenlist.values())

    yellowKeys = list(yellowlist.keys())
    yellowValues = list(yellowlist.values())

    if guess in guessesList:
        continue

    for _ in range(0, len(guessedWord)):
        if guessedWord[_] in blacklist:
            check = True

    for i in range(0, len(greenKeys)):
        if guessedWord[greenKeys[i]] != greenValues[i]:
            check = True

    for c in range(0, len(yellowKeys)):
        if guessedWord[yellowKeys[c]] == yellowValues[c] or yellowValues[c] not in guessedWord:
            check = True
    
    if check == True:
        print(guessedWord)
        continue

    print(bold + green + guessedWord + clear)
    guessesList.append(guess)
    feedback = input(f"{bold}{yellow}feedback: {clear}")

    if feedback != "done":
        for x in range(0, len(feedback)):
            if feedback[x] == "b":
                blacklist.append(guessedWord[x])
            if feedback[x] == "y":
                yellowlist.update({x: guessedWord[x]})
            if feedback[x] == "g":
                greenlist.update({x: guessedWord[x]})

    greenKeys = list(greenlist.keys())
    greenValues = list(greenlist.values())

    for y in range(0, len(greenKeys)):
        if greenlist[greenKeys[y]] in blacklist:
            if greenKeys[y] < 5:
                yellowlistKey = greenKeys[y] + 1
            else:
                yellowlistKey = greenKeys[y] - 1
            yellowlist.update({yellowlistKey: greenlist[greenKeys[y]]})
            blacklist.remove(greenlist[greenKeys[y]])
