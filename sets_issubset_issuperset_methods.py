a = {1, 2, 4}
b = {1, 2, 3, 4, 5}

# a subset is a part of a larger group of things
# a super set are the extra elements of another set plus the subset

print(b.issuperset(a))
print(a.issuperset(b))
print(a.issubset(b))
print(a < b)
print(a <= b)
print(b.issubset(a))