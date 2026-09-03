from dataclasses import dataclass
from operator import index
import random
@dataclass
class card():
    suit : str = ''
    value : int = 0
    size: float = 0.0

def build_deck():
    # setup all cards and return ten of them
    thesecards = [card() for index in range(52)]
    suits = ['hearts', 'clubs','diamonds','spades']
    count = 0
    for s in range(0,4):
        for index in range(1,14):
            thesecards[count].suit = suits[s]
            thesecards[count].value = index
            count += 1
    return thesecards

def draw_cards(thesecards):
    dealtcards = [card() for index in range(10)]
    selectednums = []
    # pick 10 to return
    for index in range(10):
        selectednum = random.randint(0,51)
        while selectednum in selectednums:
            selectednum = random.randint(0,51)
        selectednums.append(selectednum)
        dealtcards[index] = thesecards[selectednum]
    return dealtcards

def display_cards(cardarray):
    for index in range(len(cardarray)):
        output = cardarray[index].suit
        output = output + " : " + str(cardarray[index].value)
        print(output)

def initsize(cards):
    suits = ["hearts", "clubs", "diamonds","spades"]
    for card in cards:
        card.size = card.value + (suits.index(card.suit)+1)*0.1

def sort_cards(cards):
    for index in range (1,len(cards)):
#store the value to be inserted into the array
        currentvalue = cards[index]
        position = index
#shift the rest of the array one to the right
        while position > 0 and cards[position-1].size>currentvalue.size:
           cards[position] = cards[position-1]
           position -= 1


 #insert the value into the array
           cards[position] = currentvalue
    return cards


# main program
cards = [card() for index in range(10)]
allcards = [card() for index in range(52)]
allcards = build_deck()
cards = draw_cards(allcards)
display_cards(cards)
initsize(cards)
print (cards)
cards = sort_cards(cards)
print("final sorted pile:")
display_cards(cards)