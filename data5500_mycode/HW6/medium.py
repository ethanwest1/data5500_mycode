# Ethan Westenskow
# 2. Given an array of integers, write a function that finds the second largest number in the array.

# Analyze the time complexity of your solution using Big O notation, 
# especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

import random

#Generates a random list of 10 intergers for our arrary. 
numbers = [random.randint(-100,100) for _ in range(10)]
print(numbers)

def find_second_largest_num(numbers):
    # Start both as very small values
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            #Update both variables if we find a new largest.
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            # Update second_largest if it's in between
            second_largest = num
    return second_largest

print(find_second_largest_num(numbers))

##__Time Complexity = O(n), because the it only runs through the list once. The runtime grows directly with the list length. 
##__Space Complexity = O(2), since we only use a few variables regardless of input size.



# Questions I asked while working on the medium.py problem:
# 1. My function doesn't work right now, but why not?
#    def find_largest_num(numbers):
#        largest_num = numbers[0]
#        for num in range(len(numbers)):
#            if numbers[num + 1] > numbers[num]:
#                largest_num = numbers[num + 1]
#        return largest_num
# 2. Yes please. (When I asked for the logic to track the second largest as well)
# 3. That logic makes sense. Help me understand the time complexity and space complexity of this function
# 4. Why wouldn't the space complexity be O(2) because we have 2 variables now?
# 5. So if we made an additional list, then our space complexity would increase?
