# returns the first index position of a given element in a list.  

stickers = ["Sass", "Google", "Bitcoin", "Slack", "Perl", "Google"]
print(stickers)
print()
print(stickers.index("Google"))
print(stickers.index("Perl"))
print()

if "nginx" in stickers:
	print(stickers.index("nginx"))
else:
	print(False)

print()

# .index() also accepts a second parameter to specify where you want to start searching from using an number

print(stickers.index("Google", 3))