# a closure is a programming pattern in which a scope retains access to an enclosing scopes names 

# example 

def outer():
    candy = "Snickers"
    def inner():
        return candy
    return inner() # returning inner is the closure
print(outer())
print()

def multiply(a, b):

  return a * b



def divide(a, b):

  return a / b



def calculate(func, a, b):

  return func(a, b)



print(calculate(multiply, 10, 5))
print()


def a():

  def b():

    def c():

      return val

    return c()

  return b()



print(a())
val = "Hello"

