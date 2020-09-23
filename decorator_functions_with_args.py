def be_nice(fn):
    def inner(*args, **kwargs):
        print("I will execute your function for you....\n")
        fn(*args, **kwargs)
        print("Function execution completed. Have a nice day.")
        
    return inner 


@be_nice
def complex_business_logic(name):
    print(f"{name} is doing complex things....\n")

complex_business_logic("Jason")
print()


# now looking at returned values from decorated functions
def be_nice2(fn):
    def inner(*args, **kwargs):
        print("I will execute your function for you")
        output = fn(*args, **kwargs)
        print("Function execution completed.  Have a nice day.")
        return output
    
    return inner

@be_nice2
def complex_business_sum(a, b):
    return f"{a} + {b} = {a + b}"

print(complex_business_sum(5, 5))
print()


def run_twice(fn):
  def inner(*args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)
 
  return inner
 
@run_twice
def repeater(phrase):
  print(phrase)
 
repeater("Python")