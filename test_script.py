# My worker is trying to randomize the order of the roles list below. However, they find that roles remains unchanged after it being passed into the shuffle function. What is happening?



import random

roles = ["DPS", "Tank", "Healer"]

random.shuffle(sorted(roles))

print(roles) # ["DPS", "Tank", "Healer"]

