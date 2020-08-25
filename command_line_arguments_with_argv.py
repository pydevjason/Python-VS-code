import sys

print(sys.argv)

word_length = 0
for i in sys.argv[1:]:
    word_length += len(i)
print(f"the total length of all command line arguments is {word_length}")