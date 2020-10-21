import random

print(random.choice(["jason", "stephanie", "ethan"]))
print(random.choice((1, 2, 3)))

lottery_numbers = [random.randint(1, 50) for value in range(50)]

print(lottery_numbers)

print(random.sample(lottery_numbers, 5))
print()

# shuffle function requires a mutable object
# shuffle will return a NoneType if fed through the print function.  
characters = ["warrior", "druid", "hunter", "rogue", "mage"]

clone = characters[:]
random.shuffle(clone)
print()
print(characters)
print(clone)

