import copy

# these shallow copies are for using with non-nested objects.  For nested objects use deep copy
a = [1, 2, 3]

# copy of a
b = a[:]
print(b == a) # b equal to a
print(b is a) # b not identical to a
print()

c = copy.copy(a)
print(a == c)
print(a is c)
print()

numbers = [2,3,4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)

print(a == b)
print(a is b)
print(a[1] is b[1]) # here we can see that this is only a shallow copy as the identities of the nested items of a and b are the same
print()


pizza = ["Crust", "Tomato Sauce", "Cheese"]
lunch = pizza
breakfast = ["Crust", "Tomato Sauce", "Cheese"]
 
print(pizza is lunch)
print(lunch is breakfast)