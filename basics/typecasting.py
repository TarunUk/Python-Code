#TypeCasting : The process of converting a variable from one data type to another
#                str(), float(), int(), bool()

name = "Tarun Rajput"
age = 23
cgpa = 7.5
is_student = True

#Just to check the type
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

#convert one type to another

cgpa = int(cgpa)
print(cgpa)

age = float(age)
print(age)

name = bool(name)
print(name)

