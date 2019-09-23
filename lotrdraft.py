from collections import Counter
from random import shuffle
import pyperclip

version = "0.1.1"

def pickHero(heroSet):
    shuffle(heroBase)
    currentPick = heroBase[:heroOptions]
    print('\nChoose from these options.')
    for i in range(heroOptions):
        print("{}. {}".format(i+1, currentPick[i][0]))
    a = input()
    while a not in [str(i+1) for i in range(heroOptions)]:
        print('Come again?')
        a = input()
    a = int(a)-1
    heroBase.remove(currentPick[a])
    heroSet.append(currentPick[a])
    return heroSet

def pick(number, currentDeck, cardBase):
    shuffle(cardBase)
    currentPick = cardBase[:cardOptions]
    print('\n{}. Choose from these options.'.format(number+1))
    for i in range(cardOptions):
        print("{}. {}".format(i+1, currentPick[i][0]))
    a = input()
    while a not in [str(i+1) for i in range(cardOptions)]:
        print('Come again?')
        a = input()
    a = int(a)-1
    currentDeck[currentPick[a][0]] += 1
    if currentDeck[currentPick[a][0]] == 2:
        cardBase.remove(currentPick[a])
    return currentDeck, cardBase

dump = ""

heroOptions = 3
cardOptions = 3

cardBaseFile = open('lotracgcards.txt').readlines()
heroBase = []
cardBase = []
for line in cardBaseFile:
    stats = line.strip().split('|')
    if len(stats) == 2:
        heroBase.append(stats)
    else:
        cardBase.append([stats[0], stats[1], int(stats[2])])

heroSet = []
for i in range(3):
    pickHero(heroSet)
dump += "Heroes: {} & {} & {} ({}{}{})\n\n".format(heroSet[0][0], heroSet[1][0], heroSet[2][0], heroSet[0][1], heroSet[1][1], heroSet[2][1])
sphereChoice = Counter()
for hero in heroSet:
    sphereChoice[hero[1]] += 1
cuts = []
for card in cardBase:
    if sphereChoice[card[1]] < card[2]:
        cuts.append(card)
cardBase = [item for item in cardBase if item not in cuts]

currentDeck = Counter()
for i in range(30):
    currentDeck, cardBase = pick(i, currentDeck, cardBase)
for card in sorted(currentDeck.keys()):
    dump += "{} {}\n".format(currentDeck[card], card)

dump += '\nDeck drafted via the LotR ACG DraftSim v{} (https://github.com/L3murCatta/lotracgdraftsim)'.format(version)

print('Your deck was copied to clipboard!\n')
print('Press any button to exit...')
input()

pyperclip.copy(dump)
