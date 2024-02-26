import re
import sqlite3
import pandas



def input_check():
        
        
        while True:
            special = set('[@_!#$%^&*()<>?/|}{~:]')

            pick = input("Please pick a letter: ")
            if any((s in special) for s in pick):
                print("Special characters not accepted. Try again.")
                continue
            if any(a.isdigit() for a in pick):
                print("Numbers are not accepted. Try again.")
                continue
            if len(pick) > 1:
                print("Please enter only one letter")
                continue
            else:
                return pick

        
def create_tables():
    connection = sqlite3.connect('leaderboards.db')
    cur = connection.cursor()
    create_table = '''CREATE OR REPLACE TABLE 4_letters_leaderboard(
                      player varchar(50),
                      word varchar(4),
                      guesses int,
                      total_time);'''
    try:
        cur.execute(create_table)
    except sqlite3.DatabaseError: 
         print("Create already created")
    else:
         print("Table created")
         connection.commit()
    connection.close()


def player_score(player, word, guesses, time):
    connection = sqlite3.connect('leaderboards.db')
    cur = connection.cursor()    
    insert = f"INSERT INTO Leaderboard VALUES ({player}, {word}, {guesses}, {time});" 
    try:
        cur.execute(insert)
    except sqlite3.DatabaseError:
        print("Error adding score to table")
    else:
        print("Score added")
        connection.commit()
        connection.close()