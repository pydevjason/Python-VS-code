def add_positive_nums(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive!")
        return a + b
    except ValueError as e:
        return f"Caught ValueError: {e}"

print(add_positive_nums(2, -2))
