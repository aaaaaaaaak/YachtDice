import random

save = {}
dices = {"dice1" : 0, "dice2" : 0, "dice3" : 0, "dice4" : 0, "dice5" : 0}

for dice in dices:
    dices[dice] = random.randint(1, 6)

print(dices)