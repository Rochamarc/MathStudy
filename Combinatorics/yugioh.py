# A chance of drawing the entire Exodia set in your very first opening hand 
# is 1 in 658,008 (roughly 0.00015%) for the first player in a standard 40-card deck.

# In Yu-Gi-Oh!, you can have one copy of each of the five Exodia pieces in your 40-card deck.
# When you have all five pieces in your hand, the game ends and you are considered the winner of the duel.
# Let's write some code to simulate games. Starting with five cards in your hand, let's see if it is possible
# to draw all five of these cards into your hand.

# Rules
# This is the deck
# 1 Anchamoufrite
# 1 Exodia the Forbidden One
# 1 Left Arm of the Forbidden One
# 1 Left Leg of the Forbidden One
# 1 Right Arm of the Forbidden One
# 1 Right Leg of the Forbidden One
# 3 Royal Magical Library
# 1 Card of Demise
# 1 Chicken Game
# 1 Contract with Don Thousand
# 3 Cursed Bamboo Sword
# 1 Dark Factory of Mass Production
# 1 Dark World Dealings
# 1 Double Summon
# 3 Golden Bamboo Sword
# 1 Into the Void
# 3 Magical Citadel of Endymion
# 2 Magical Mallet
# 1 Magical Stone Excavation
# 1 One Day of Peace
# 1 Pot of Duality
# 1 Spell Power Grasp
# 1 Terraforming
# 1 Toon Bookmark
# 3 Toon Table of Contents

import random
from time import sleep

deck = [
    "Anchamoufrite",
    "Exodia the Forbidden One",
    "Left Arm of the Forbidden One",
    "Left Leg of the Forbidden One",
    "Right Arm of the Forbidden One",
    "Right Leg of the Forbidden One",
    "Royal Magical Library",
    "Royal Magical Library",
    "Royal Magical Library",
    "Card of Demise",
    "Chicken Game",
    "Contract with Don Thousand",
    "Cursed Bamboo Sword",
    "Cursed Bamboo Sword",
    "Cursed Bamboo Sword",
    "Dark Factory of Mass Production",
    "Dark World Dealings",
    "Double Summon",
    "Golden Bamboo Sword",
    "Golden Bamboo Sword",
    "Golden Bamboo Sword",
    "Into the Void",
    "Magical Citadel of Endymion",
    "Magical Citadel of Endymion",
    "Magical Citadel of Endymion",
    "Magical Mallet",
    "Magical Mallet",
    "Magical Stone Excavation",
    "One Day of Peace",
    "Pot of Duality",
    "Spell Power Grasp",
    "Terraforming",
    "Toon Bookmark",
    "Toon Table of Contents",
    "Toon Table of Contents",
    "Toon Table of Contents"
]

def check_hand(your_hand: list) -> int:
    """
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
        if i in winning_hand:
            cont += 1

    return cont

for it in range(100_000):
    your_deck = deck.copy()
    random.shuffle(your_deck)
    your_hand = your_deck[1:6] 

    print(*your_hand, sep=" | ", end="\n")
    sleep(0.1)
    
    if check_hand == 5:
        print("Yupii!!!!!!")
        break


    