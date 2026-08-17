#input():   A function that prompts the user to enter data and return the entered data as a string.

name = input("Enter your name?: ")
age = int(input("How old are you?: "))

print(f"My name is {name}")
print(f"I am {age} years old.")



#Exercise

l = float(input("Enter the length of rectangle?: "))
r = float(input("Enter the radius of rectangle?: "))

area = l * r

area = int(area)

print(f"The area is: {area}cm")


#exercise

item = (input("What item would you like to but?: "))
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"The total price is ${total}")
