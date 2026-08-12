def decorator(func):
    def wrapper():
        print("Hi my name is tarun")
        print("From lpu punjab")
        func()
        #print("I am 22 years old")

    return wrapper

@decorator
def loc():
    print("I am from india")

def age():
    print("I am 22 years old")

def addre():
    print("Currently lives in punjab")

def study():
    print("pursuing btech in cse")

loc()
age()
addre()
study()
