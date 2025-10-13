#Ethan Westenskow

lst = [3, 1, 4]

## my failed attempt
# sorted_lst = [1]
# for x in range(len(lst)):
#     current_var = lst[x]
#     if current_var > sorted_lst[-1]:
#         sorted_lst.insert(-1,current_var)
#     else:
#         sorted_lst.insert(-2,current_var)

# print(sorted_lst)

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        #compare two elements and swap if element 1 is greater.
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst [i]
    print(lst)
print('bubble sort: ', lst)