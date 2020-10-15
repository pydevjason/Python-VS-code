# things tuples and lists have in common:  They both have a len(), they both support indexing, 

ss = (123, 45, 6789)
print(len(ss))
print(ss[0])
print(ss[-1])
print(ss[-2])
print(ss[-3])
print()

print()


# if a given tuple has another data structure inside it such as a list, the list inside the tuple is mutable but the tuple remains immutable.  The list elements inside the tuple can be modified.

places = (
	["my home", "air", "water"],
	["someone elses home", "wind", "acetylcholine"],
	)

places[0][0] = "be"
print(places)
print()


