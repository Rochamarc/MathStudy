

with open("exodia_deck.csv", "r") as file:
    file = file.readlines()

    for line in file:
        line = line.split(",")
        card = line[0].replace(r"'", "")
        print(card)