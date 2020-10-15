story = "once upon a time"

print(story.capitalize())
print(story.title())
print(story.upper())
print(story.lower())

new_story = "OnCe uPoN a TiMe"
print(new_story.swapcase())

# always remember that each one of these methods creates a new string object as strings are immutable.  This can be verified using the id() function on each object
print(id(story))
print(id(story.title()))