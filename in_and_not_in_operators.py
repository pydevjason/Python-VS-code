# using the in and not in operators to check for inclusion and exclusion.
# in and not in return booleans

announcement = "The winners of the prize are Boris, Andy, and Adam."

print("Boris" in announcement)
print("Steven" in announcement)
print("boris" in announcement)
print(" " in announcement)
print("," in announcement)

print()

# not in returns the inverse of in
print("Boris" not in announcement) # false
print("Steven" not in announcement) # true
print("boris" not in announcement) # true
print(" " not in announcement) # false
print("," not in announcement) # false