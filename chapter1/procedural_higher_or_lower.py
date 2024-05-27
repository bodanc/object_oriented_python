import random

TUPLE_SUIT = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
TUPLE_RANK = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

N_CARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print('Welcome to Higher or Lower!')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start with.')
print()

startingDeckList = []

for suit in TUPLE_SUIT:
    for thisValue, rank in enumerate(TUPLE_RANK):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
