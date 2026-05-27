#Step 1: Take number of elements from user
n = int(input("Enter the number of elements: "))

#step 2: Create an empty list
arr = []

#step 3: Take elements as input from user
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))  # add each element into the list

#step 4: Initialize sum with 0
sum = 0

#srep 5: add all elements of list into sum
for i in range(n):
    sum += arr[i]
#step 6: print the final sum

print("Sum of array: ",sum)