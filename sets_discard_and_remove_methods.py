# .discard() and .remove() do the same thing to remove an element from a set but with one difference.  The remove method will return a key error if the element is not found whereas the discard method will not raise an error and just move on.

# example 1

agents = {"Smith", "Neo", "Trinity", "Oracle"}

agents.remove("Neo")
print(agents)
print()

# no error was encountered using the discard method as Skinner is not present in the set
agents.discard("Skinner")
print(agents)

