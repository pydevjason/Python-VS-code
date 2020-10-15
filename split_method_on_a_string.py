# .split() and .join() are complimentary methods invoked on string objects
# the split separates a string on the occurance of a delimiter and returns a list data structure
# split also accepts a second parameter maxsplit which limits the number of splits

names = "Bob, Mac, Vic, Rick, Dick"
print(names.split(", "))
print(names.split(", ", 2))
print()

sentence = "I am still learning Python"
words = sentence.split(" ")
count = 0
for i in words:
	count += len(i)
print(f"there are {count} letters in the sentence")

