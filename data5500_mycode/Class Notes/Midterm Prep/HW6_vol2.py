# #Code for Big O notations N, Log N, N^2
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# # N - Looping through a list once
# for x in lst:
#     print(x * x)

# # Log N - Binary Search in sorted list
# n = len(lst)
# while n > 1:
#     print('Current Size: ', n)
#     n = n//2

# # N^2 - nested loops
# for x in range(len(lst)):
#     for x in range(len(lst)):
#         print(x, "+",x, "=", x+x)



# 1. Given an array of integers, write a function to calculate the sum of all elements in the array.

# Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.abs
import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10])
total = 0
for x in range(len(arr)):
    total += arr[x]
# print(total)

# 2. Given an array of integers, write a function that finds the second largest number in the array.

# Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

arr = np.array([47, 12, 89, 5, 63, 22, 78, 36, 91, 10])


largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        #Update both variables if we find a new largest.
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        # Update second_largest if it's in between
        second_largest = num
print(second_largest)


