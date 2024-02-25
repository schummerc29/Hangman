import reader

final = reader.randomize_word()
tries = 10
guesses = 0

# Parse word in separate characters
word = str(final)
wordList = list(word)
playerWord = "_"*len(word)
playerWordList = list(playerWord)

while True:
    s = ''
    word = s.join(playerWordList)
    print(f"Current word: {word}")

    try:
        pick = input("Please pick a letter: ")
    except TypeError:
        print("Please provide a valid input")
    
    print(f"You picked: {pick}")
    counter = 0
    index = 0

    for letter in wordList:
        if pick.lower() == letter.lower():
            playerWordList[index] = pick
            index += 1
            counter += 1
        else:
            index += 1

    guesses += 1
    # Check if there are any letters left to find:
    blank = '_'
    if blank in playerWordList:
        if counter > 0:
            print(f"{pick} is in the word {counter} time(s)!")
            continue
        else:
            tries -= 1
            print(f"{pick} was not in the word!")
            if tries > 1:
                print(f"You have {tries} tries left!")
            if tries == 1:
                print(f"You have {tries} try left!")
            if tries == 0:
                print("You're all out of attempts!")
                print(f"The correct answer was '{word}'!")
                break
    else:
        word = s.join(playerWordList)
        print(f"You've won! The correct answer is {word.upper()} and it took you {guesses} guesses!") 
        break    