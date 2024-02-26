import csv
import json 
import os
import random

with open('4_letter_words.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('4words.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

def random_word():
    with open('4words.json', 'r') as file:
        datastore = json.load(file)
    value = random.choice(datastore)
    return value['word']