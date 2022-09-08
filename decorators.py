#  A decorator is a function that add functionalilty to an already made function

# def addTwoNumbers(a, b):
#     return a + b

# DECORATOR function
def Logger(func):
    def wrapper(*args, **kwargs):
        print("function Executed")
        func(*args, **kwargs)
        print("function Execution finished")

    return wrapper


@Logger
def addTwoNumbers(a, b):
    return a + b


print(addTwoNumbers(1, 2))
