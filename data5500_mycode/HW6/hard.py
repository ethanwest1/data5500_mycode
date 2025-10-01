#Ethan Westenskow
# 
# 3. Write a function that takes an array of integers as input and returns the maximum difference 
# between any two numbers in the array.

# Analyze the time complexity of your solution using Big O notation, 
# especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

import random

#Generates a random list of 10 intergers for our arrary. 
numbers = [random.randint(-100,100) for _ in range(10)]
print(numbers)

def max_difference(numbers):
    difference = max(numbers) - min(numbers)
    return difference

print(max_difference(numbers))

##__Time Complexity = O(n), because the it only runs through the list once. The runtime grows directly with the list length. 
##__Space Complexity = O(1), since we only use one variable regardless of input size.

def max_difference_bruteforce(numbers):
    max_diff = float('-inf')
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(max_difference_bruteforce(numbers))

##__Time_Capacity = O(n), because we run through each element of the array once so it will grow with the size of the array.
##__Space_Capacity = O(1), because we only store the memory in one variable regardless of the array size. 



#Questions that I asked chatgpt for this problem. 
# Questions I asked while working on the hard.py problem:
# 1. This is the function that made the most sense to me, but give me the code for the brute way, 
#    but don't give me the big o notation, I want to figure that out on my own.
#
#    My function:
#    def max_difference(numbers):
#        difference = max(numbers) - min(numbers)
#        return difference
#"So for time complexity, our function would be O(n) because it runs once for each item in the list?"
# "Is this correct for the big o notation? 
# 
# ##__Time_Capacity = O(2), because we run through the array twice as the function runs.
# ##__Space_Capacity = O(1), because we only store the memory in one variable regardless of the array size."
# 
# "Yes, explain why constants don't matter in Big-O function please"
# "No, but thank you for correcting me. Give me the questions that I asked you for this question in python comments please."