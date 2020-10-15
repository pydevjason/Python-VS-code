class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some method")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

# using the above syntax with the double underscores prefixing some attribute and some method, these objects are not easily accessible any more, however, they can be accessed by using a single underscore before the class name.

print(n._Nonsense__some_attribute)
print(sn._Nonsense__some_attribute)
n._Nonsense__some_method()
sn._Nonsense__some_method()
