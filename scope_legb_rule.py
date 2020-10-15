# LEGB, Local Encolsing Global Built-in

def outer():
    x = 10
    
    def inner():
        x = 5
        return x
    
    return inner()

print(outer())
# the outer returns 5 because we are returning inner in the outer function

print()
def outer2():
    a = 10
    
    def inner2():
        return a
    
    return inner2()

print(outer2())

# here, the outer returns the outer a = 10 because there is a is not defined in the inner2 function, so Python moves to the enclosing level to find a where the value being stored is 10
print()

c = 15
def outer3():
    def inner3():
        return c
    return inner3()
print(outer3())
print()
# here c = 15 in the global namespace because there is no value defined in the local or enclosing namespace.  c is returning 15 because Python sees nothing defined for c in the enclosing or local area

def outer4():
    def inner4():
        return len
    return inner4()
print(outer4()("Python"))
print()
# here Python returns the built-in function len 

value = 10
 
def a():
  value = 20
 
  def b():
    value = 30
    return value
  
  return b()

print(a())