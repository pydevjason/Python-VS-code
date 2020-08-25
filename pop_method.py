import sys

print(sys.version)

metals = ["stainless", "zinc", "aluminum", "copper", "titanium"]
print(metals)
print()

last_metal = metals.pop()
print(last_metal)
print()

# .pop() accepts one argument an index position to specify what element to "pop" off the list.

zinc = metals.pop(1)
print(metals)
print()
print(zinc)
print()

copper = metals.pop(-1)
print(metals)
print()
print(copper)

# "shell_cmd": "python -u \"$file\"",
# "shell_cmd": "python -m py_compile \"${file}\"",




