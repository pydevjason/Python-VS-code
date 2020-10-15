# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0

def vowel_count(string):
    return string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")

print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))

print()

def vowel_count2(string):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

print(vowel_count2("estate"))
print(vowel_count2("helicopter"))
print(vowel_count2("ssh"))

print()

# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1


def find_my_letter(string, char):
    return string.find(char)

print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))