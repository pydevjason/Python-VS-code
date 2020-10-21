# here in the docstring we are running a test or check of the function and it's arguments to determine correct or incorrect output 

def sum_of_list(numbers):
    """Return the sum of all numbers in a list.
    >>> sum_of_list([1,2,3])
    6
    >>> sum_of_list([5,8,13])
    26
    """
    total = 0
    for i in numbers:
        total += i
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()