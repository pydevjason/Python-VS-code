# the remove method removes an element from list by its value, not by its index position.

programming_languages = ["Python", "Golang", "C#", "Java", "SQL", "Swift"]

print(programming_languages)
print()

programming_languages.remove("SQL")
print(programming_languages)
print()

# if there are two of the same elements in a list, you can invoke .remove() again and it will remove the second occurance of the element

# using the .clear() method.  clears all elements from a list resulting in an empty list

programming_languages.clear()
print(programming_languages)