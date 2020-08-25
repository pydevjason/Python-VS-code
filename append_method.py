laptop_brands = ["HP", "Apple", "Lenovo", "Dell", "System 76"]
print(laptop_brands)
print(len(laptop_brands))
print()

laptop_brands.append("Asus")
print(laptop_brands)
print(len(laptop_brands))
print()

# by doing this we have not created a new list but rather mutated the original data structure
# .append() will return None if stored inside a variable

