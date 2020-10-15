# diamond-shaped inheritance 
class FilmMaker():
    def give_interview(self):
        print("I love making movies")

class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")

class JackOfAllTrades(Director, ScreenWriter):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

print(JackOfAllTrades.mro())
print()

class A():
  def dispatch(self):
    return "apple"
 
class B(A):
  pass
 
class C(A):
  def dispatch(self):
    return "banana"
 
class D(B, C):
  pass
 
my_obj = D()
print(D.mro())
print(my_obj.dispatch())