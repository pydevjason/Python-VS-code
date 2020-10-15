alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2])

# lines 7-10 accomplish the same result with different ways of expressing it

print(alphabet[0:26:3])
print(alphabet[:26:3])
print(alphabet[0::3])
print(alphabet[::3])
print()

# reverse string
print(alphabet[::-1])