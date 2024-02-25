import csv
import json 
import os
from random import randint

with open('4_letter_words.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('4words.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

def random_word():
    with open('4words.json', 'r') as file:
        data = json.load(file)

        num = randint(0, len(data) - 1)

        
        for word in data:
           if word.get('number') == num:
                final = word['word']
                print(final)
       
        

print(random_word())