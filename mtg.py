import json
import random
import os
import random
os.chdir(os.path.dirname(__file__))

def findCard(name, allCardsDictionary):
    # ensure case insensitivity
    name = name.lower()
    for this_key in allCardsDictionary.keys():
        if name == this_key.lower():
            name = this_key
    card = allCardsDictionary[name]
    return card

def buildDeck(filePath, allCardsDictionary):
    # load the file
    file_object2 = open(filePath, 'r', encoding='utf-8')
    all_lines = file_object2.readlines()
    file_object2.close()
    deck = list()
    # for every line of the file, find the card and how many times it is in the deck
    for this_line in all_lines:
        # notate string and amount in text file when reading lines
        splitLine = this_line.split()
        amountString = splitLine[-1]
        cardName = splitLine[0:-1]
        cardName = ' '.join(cardName)
        # drop the x on amountString
        amountString = amountString[1:]
        # remove the new line white space
        amountString = amountString.strip()
        # convert the string to an integer
        amount = int(amountString)
        # then add it to the deck that many times
        card = findCard(cardName, allCardsDictionary)
        deck += list(card) * amount
    # return the deck
    return deck


def lookinGood(deck):
    colorTranslator = {
        'B': 'Black',
        'W': 'White',
        'U': 'Blue',
        'R': 'Red',
        'G': 'Green'
    }
    # takes a deck(list of dictionaries) and prints the name of every card in it
    for everyDict in deck:
        colorsList = list()
        colorsList = everyDict['colors']
        colors = ' '.join([colorTranslator[i] for i in colorsList])
        if colors == '':
            colors = 'Colorless'
        name = everyDict['name']
        print(f'{name} ({colors})')


file_object = open('AtomicCards.json', 'r', encoding='utf-8')
full_json = json.load(file_object)
file_object.close()
all_cards = full_json['data']

piDeck = buildDeck('Deck/pie_green_black_deck.txt', all_cards)
random.shuffle(piDeck)
lookinGood(piDeck[:7])

# idea for mulligan function
# load new decks
# modify decks/card information
# create new card for txt file
