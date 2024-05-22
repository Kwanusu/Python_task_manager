def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError as exception:
        print("Error:", exception)
        raise ValueError("Cannot divide by zero") from exception
    finally:
        print("Couldn't execute.")
try:
    divide_numbers(10, 2)
    divide_numbers(10, 0)
except ValueError as value_error:
    print("Error :", value_error)
