# the extend method allows to add multiple elements to the end of a list with a single method call.  

# example 1

mammal_classifications = ["marsupials", "primates", "rodents", "monotremes",]

print(mammal_classifications)
print()

mammal_classifications.extend(["cetaceans", "bears", "placentals"])
print(mammal_classifications)
print()

# using the + sign when combining lists does not mutate the list but rather returns a new list object

# the extend method mutates a list and the + returns a new list
extra_mammals = ["otters", "squirrels", "seals"]
print(mammal_classifications + extra_mammals)
print()



