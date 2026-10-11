# A chance of drawing the entire Exodia set in your very first opening hand 
# is 1 in 658,008 (roughly 0.00015%) for the first player in a standard 40-card deck.

# In Yu-Gi-Oh!, you can have one copy of each of the five Exodia pieces in your 40-card deck.
# When you have all five pieces in your hand, the game ends and you are considered the winner of the duel.
# Let's write some code to simulate games. Starting with five cards in your hand, let's see if it is possible
# to draw all five of these cards into your hand.

# Rules
# This is the deck
# Anchamoufrite
# Exodia the Forbidden One
# Left Arm of the Forbidden One
# Left Leg of the Forbidden One
# Right Arm of the Forbidden One
# Right Leg of the Forbidden One
# Royal Magical Library
# Royal Magical Library
# Royal Magical Library
# Card of Demise
# Chicken Game
# Contract with Don Thousand
# Cursed Bamboo Sword
# Cursed Bamboo Sword
# Cursed Bamboo Sword
# Dark Factory of Mass Production
# Dark World Dealings
# Double Summon
# Golden Bamboo Sword
# Golden Bamboo Sword
# Golden Bamboo Sword
# Into the Void
# Magical Citadel of Endymion
# Magical Citadel of Endymion
# Magical Citadel of Endymion
# Magical Mallet
# Magical Mallet
# Magical Stone Excavation
# One Day of Peace
# Pot of Duality
# Spell Power Grasp
# Terraforming
# Toon Bookmark
# Toon Table of Contents
# Toon Table of Contents
# Toon Table of Contents
# Upstart Goblin
# Blue-Eyes Toon Dragon
# Pseudo Space
# Trade-In

import random
from collections import defaultdict
from pprint import pprint
import pandas as pd 

dd = defaultdict(int)
winning_hands = 0

deck = []

with open("exodia_deck.csv", "r") as file:
    file = file.readlines()

    for line in file:
        line = line.split(",")
        card = line[0].replace('"', '')
        deck.append(card)

def check_hand(your_hand: list) -> int:
    """
    Check a hand for:
    "Exodia the Forbidden One"
    "Left Arm of the Forbidden One"
    "Left Leg of the Forbidden One"
    "Right Arm of the Forbidden One"
    "Right Leg of the Forbidden One"

    Parameters
    ----------
    your_hand: list
        A list of five cards from the user's deck

    Returns
    -------
    cont : int
        If value is equal to five, you win the duel. max: 5
    """

    winning_hand = [
        "Exodia the Forbidden One",
        "Left Arm of the Forbidden One",
        "Left Leg of the Forbidden One",
        "Right Arm of the Forbidden One",
        "Right Leg of the Forbidden One"
    ]

    cont = 0
    for i in your_hand:
        dd[i] += 1

        if i in winning_hand:
            cont += 1

    return cont

try:
    for it in range(1*10**7):

        # Copy the main deck, shuffle and draw first five cards
        your_deck = deck.copy()
        random.shuffle(your_deck)
        your_hand = your_deck[1:6] 

        print("Running on {}".format(it), end="\r")

        # Hit a winning hand
        if check_hand(your_hand) == 5:
            print("We've assembled all five special cards... all five pieces of the puzzle!")
            print("We have a match at {}".format(it))
            winning_hands += 1

except KeyboardInterrupt:  
    print("Exiting the program!!!")

# Report
report = []

for key, value in dd.items():
    report.append([key, value])

# Dataframe report
df = pd.DataFrame(report, index=None, columns=['Card', 'Draws'])
print(df.sort_values(by='Draws'))

print("The number of winning hands is {}".format(winning_hands))

# pprint(dd)