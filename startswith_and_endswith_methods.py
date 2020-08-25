# these methods will return a boolean value

salutation = "Mr. Jason Williams"

print(salutation.startswith("M"))
print(salutation.startswith("Mr"))
print(salutation.startswith("Mr."))
print(salutation.startswith("m"))
print(salutation.startswith("mr."))
print(salutation.startswith("Jas"))
print(salutation.startswith("Mr. Jas"))

# the complimentary method to this is the .endswith() and does the inverse of .startswith()
print()
print(salutation.endswith("s"))
print(salutation.endswith("ms"))
print(salutation.endswith("iams"))
print(salutation.endswith("Liams"))

