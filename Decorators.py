def decorator(func):
    def wrapper():
        print("Hi my name is tarun")
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

loc()
age()
addre()
