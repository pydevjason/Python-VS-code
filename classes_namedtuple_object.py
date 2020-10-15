import collections
# the namedtuple object must be imported from the collections module, this is a procedure by which we can instantiate a class with only attributes but no methods.  This has interoperability of both a tuple and a class in that it can be indexed and by using dot notation the attribute can be referrenced 

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitz")

print(animal_farm[0])
print(animal_farm.title)
print()
print(gatsby.title)
print(gatsby[1])
print()

# Use the namedtuple function to create a GymExercise class whose instances
# will have three attributes: name, weight, and reps.

# Assign a squat variable to a GymExercise tuple object with 
# a name of “squat”, a weight of 265, and a rep count of 3.

# Assign a bench variable to a GymExercise tuple object with 
# a name of “benchpress”, a weight of 185, and a rep count of 5.

# Assign a deadlift variable to a GymExercise tuple object with
# a name of “deadlift”, a weight of 225, and a rep count of 6.

# Assign a press variable to a GymExercise tuple object with 
# a name of “press”, a weight of 120, and a rep count of 8.


GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])

squat = GymExercise("squat", 265, 3)
benchpress = GymExercise("benchpress", 185, 5)
deadlift = GymExercise("deadlift", 225, 6)
press = GymExercise("press", 120, 8)


print([squat.name, squat.weight, squat.reps])






















