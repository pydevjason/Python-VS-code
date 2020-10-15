# the sort method sorts a list in place in either ascending or alphabetical depending on the data structure that is using the .sort() method

numbers = [3, 45, 10, 78, 1, 2, 23]
numbers.sort()
print(numbers)
print()

letters = ["w", "v", "b", "o", "l", "a", "q"]
letters.sort()
print(letters)
print()

# to make them in descending order simply call the reverse method after sort

letters.reverse()
print(letters)
print()
# using the sorted() function returns a new list instead of mutating an original list

numbers = [9, 2, 8, 3, 7, 4, 6, 5, 1]
print(sorted(numbers))
print()

countdown = [5, 3, 8, 1, 10, 2]
countdown.sort()
countdown.reverse()
print(countdown)
print()

songs = ["Proven", "Perseverance", "Defeatist", "Puritan"]
songs[1:3] = ["I Will Be Heard"]
print(songs)
print()

spices = ["paprika", "nutmeg", "ginger", "cinnamon", "turmeric"]
spices.append(["garlic", "berbere", "sansho"])
print(spices)