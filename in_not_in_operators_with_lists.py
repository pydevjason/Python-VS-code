# using the in operator
print("boat" in "speedboat")
print("osmo" in "osmolarity")

print()

photography = ["wedding", "food", "astro"]
print("wedding" in photography)
print("cyborg" in photography)
print("Astro" in photography)

print()

floats = [23.3, 124.9, 15.1, 78.78, 1.2, 10.0]
print(45.3 in floats)
print(1.2 in floats)
print(124 in floats)
print(10 in floats)

print()
# using the not in operator
print("wedding" not in photography)
print("toxoplasmosis" not in photography)
print(124.9 not in floats)
print(909.2 not in floats)

print()
# using conditional logic on lists

if "toxoplasmosis" not in photography:
    print("It's true, toxoplasmosis is not in photography")
else:
    print("This will never print")