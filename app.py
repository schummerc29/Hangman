import reader
import functions
import time
import sqlite3

final = reader.random_word()
tries = 10
guesses = 0

# Parse word in separate characters
word = str(final)
wordList = list(word)
playerWord = "_"*len(word)
playerWordList = list(playerWord)

player = input("Please enter your name: ")

while True:
    time_start = time.time()
    s = ''
    word = s.join(playerWordList)
    print(f"Current word: {word}")

    pick = functions.input_check()
    
    print(f"You picked: {pick}")
    counter = 0
    index = 0

    for letter in wordList:
        if pick.lower() == letter.lower():
            playerWordList[index] = pick.lower()
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
                print(f"The correct answer was '{final}'!")
                break
    else:
        time_stop = time.time()
        total = time_stop - time_start
        word = s.join(playerWordList)
        print(f"You've won! The correct answer is {final.upper()} and it took you {guesses} guesses!") 
        
   
        sqliteConnection = sqlite3.connect('leaderboards.db')
        cursor = sqliteConnection.cursor()
        insert = f'''INSERT INTO Leaderboard (Player, Word, Guesses, Time) 
                    VALUES ('{player}', '{word.upper()}', {guesses}, {total});'''
        cursor.execute(insert)
        sqliteConnection.commit()
        cursor.close()
        break  

    