#!/usr/bin/env python
# coding: utf-8

# ```
# Task : Print the prime numbers which are between 1 to entered limit number (n).
# 
# You can use a nested for loop.
# 
# Collect all these numbers into a list
# 
# 
# The desired output for n=100 :
# 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
# ```

# In[1]:


prime_list = []
for q in range(2,100):
    isprime = True
    for j in range(2, q):
        if q % j == 0 :
            isprime = False
    if isprime:
        prime_list.append(q)
print(prime_list)

