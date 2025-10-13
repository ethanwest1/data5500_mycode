# Ethan Westenskow

#____Recursion
# When a function calls itself

# 4 Parts to a recursive funciton:
    # 1. Function definition
    # 2. Base case
    # 3. Logic
    # 4. Recursive Call

#### 
# Recursive Example 1
# Printing numbers iterative
nums = [3, 1, 4, 1, 5, 9, 2, 6]

for i in range(len(nums)):
    print(nums[i])
    
# Printing numbers recursively
def print_nums(nums, i): #Function Definition
    if i >= len(nums): # X /\ (Base Case, this shuts down the function. Ends the loop)
        return
    
    print(nums[i]) #Logic
    print_nums(nums, i+1)
    
print_nums(nums, 0) #Recursive call

#### 
# Recursive Example 2
# Sum numbers iteratively
def sum_numbers(n):
    # add up all the numbers 1 to n, and return the result
    val = 0
    for i in range(1,n+1):
        val += i
    return val

print(sum_numbers(5)) # 15

# Sum numbers recursively
def sum_number_rec(n):
    if n == 1:
        return 1
    return n + sum_number_rec(n-1) # 5 + 4 + 3 + 2 + 1 (THE LOGIC AND THE RECURSIVE CALL)
    
print(sum_number_rec(5))
