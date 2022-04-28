#!/usr/bin/env python
# coding: utf-8

# ```
# Define a function named my_min to find the min of the inputted numbers.
# For example:
# 
# Test	                                    Result
# print(my_min(5,6,7))                           5
# print(my_min(3,8,-9,0,12,1.2))                -9
# print(my_min(-100))                           -100
# ```

# In[2]:


def my_min(*arg):
    
    inputted_num_list = [*arg]
    
    min_of_given_num = min(inputted_num_list)
    
    return min_of_given_num 

print(my_min(5, 6, 7))
print(my_min(3, 8, -9, 0, 12, 1.2))
print(my_min(-100))


# ```
# Define a function named my_sum to return the sum of all int type inputted numbers.
# 
# For example:
# 
# Test	                                            Result
# print(my_sum(9, 1, 3, 0, -1))                         12
# print(my_sum(5, 7, 4))                                16
# print(my_sum(10, -20, 30, 40))                        60
# ```

# In[3]:


def my_sum(*arg):
    given_num_list = [*arg]
    sum = 0
    for i in given_num_list:
        sum += i
    return sum  # sum of given numbers

    
print(my_sum(9, 1, 3, 0, -1))
print(my_sum(5, 7, 4))
print(my_sum(10, -20, 30, 40)) 

