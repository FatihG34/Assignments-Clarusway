#!/usr/bin/env python
# coding: utf-8

# ```
# Task : Find out the most frequent number and its frequency.
# 
# Write a program that;
# 
# Finds out the most frequent number in the given list.
# Calculates its frequency.
# Prints out the result such as :
# Given list	
# numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# Desired Output
# the most frequent number is 3 and it was 4 times repeated
# ```

# In[1]:


def most_frequent(numbers):
    counter = 0
    num = numbers[0]
     
    for i in numbers:
        curr_frequency = numbers.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

cr_frequency = numbers.count(3)
cr_frequency

output = f"The most frequent number is {most_frequent(numbers)} and  it was {cr_frequency} times repeated"
print(output)

