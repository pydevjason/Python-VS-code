# isinstance() used for determining whether a given object is made from a specific class.  issubclass() used for determining whether a class is a subclass from another class

print(type({"a": 1}))

print(isinstance({}, dict))
print(isinstance([1,2,3], list))
print(isinstance(23.12, float))
print(isinstance({1,2,3}, set))
print(isinstance(1, object))
print(isinstance((1,), tuple))
print(isinstance("jason", str))
