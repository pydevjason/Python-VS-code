class Restuarant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}.")

class Steakhouse(Restuarant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}.")

class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)

# by default, Python will take the depth-first search approach when determining method hierarchy