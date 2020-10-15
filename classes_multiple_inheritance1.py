class FrozenFood():
    def thaw(self, minutes):
        print(f"thawing for {minutes} minutes...")

    def store(self):
        print("putting in the freezer")

class Dessert():
    def add_weight(self):
        print("putting on the pounds")

    def store(self):
        print("putting in the fridge")

class IceCream(Dessert, FrozenFood):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store() # Python will look to the first object passed into IceCream subclass to determine which store method is invoked on the IceCream object

# How to determine the order of execution for method invocation?  We can use the mro() class method (takes no arguments) which shows the lookup order of classes in a list.  mro stands for method resolution order

print(IceCream.mro())