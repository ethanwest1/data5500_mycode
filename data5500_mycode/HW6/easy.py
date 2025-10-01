#Ethan Westenskow

# 1. Given an array of integers, write a function to calculate the sum of all elements in the array.

# Analyze the time complexity of your solution using Big O notation, 
# especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

import random

#Generates a random list of 10 intergers for our arrary. 
numbers = [random.randint(-100,100) for _ in range(10)]
print(numbers)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list(numbers))

## ____Time Complexity = O(n). This is because the function runs once for each item in the list. n represents the number of variables within the array. 
##_____Space Complexity = O(1). Because our memory remains constant because we only use one variable 'total'. It doesn't grow with the array. 


#### ________ ChatGPT Questions:
# 1. Give me some code to generate a list of random integers
# 2. Let's get back to the easy.py question. Don't give me any code unless I ask you for it
# 3. Does this function work?
#    def sum_list(list):
#        sum = 0
#        for num in list:
#            sum += num
#        return sum
# 4. I made a few small changes. Now that I have the code written, how do I analyze the time complexity of our solution?
# 5. So for time complexity, our function would be O(n) because it runs once for each item in the list?
# 6. Would our function’s space complexity be O(1) because we only save the memory in one variable, so it doesn't grow as our array increases?