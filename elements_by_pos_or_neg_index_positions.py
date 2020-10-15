# lists and strings are iterable, and can have substrings extracted by index position

print("omnipotent"[5])

operating_systems = ["Windows", "MAC OS", "Linux"]
print(operating_systems[0])
print(operating_systems[2])
print(operating_systems[1])
# print(operating_systems[3]) # this will raise IndexError
print()
# to access a substring of an element inside the list:
print(operating_systems[0][0])
print(operating_systems[2][4])
print(operating_systems[1][2])
print()
# same output using for loop to iterate over a list, also using enumerate() to print out index position alongside values
for i,v in enumerate(operating_systems):
    print(i,v)

print()
# using negative indices to retrieve elements and substrings from elements on a list
smart_phones = ["iPhone", "Galaxy", "Black Phone"]
print(smart_phones[-1])
print(smart_phones[-2])
print(smart_phones[-3])
print(smart_phones[-3][0])
print(smart_phones[-2][1])
print(smart_phones[-3][2])