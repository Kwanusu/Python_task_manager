# This is a block of code that enables code to run even if a section has errors
#If there is an error the exception will be executed instead of throwing an error.abs
x = 25
y = 5
  
def divide(x, y):
    try: 
        result = x / y 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print("Yeah ! Your answer is :", result) 
    finally:   
        print('This is always executed')   
divide(3, 2) 
divide(3, 0) 
  