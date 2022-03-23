#!/usr/bin/env python
# coding: utf-8

# In[1]:


f_b_list = list(range(1,101))
for i in f_b_list:
    if i % 3 == 0 and i % 5 == 0 :
        f_b_list[f_b_list.index(i)] = "FizzBuzz"
    elif i % 5 == 0:
         f_b_list[f_b_list.index(i)] = "Buzz"
    elif i % 3 == 0 : 
         f_b_list[f_b_list.index(i)]= "Fizz"
print(f_b_list)

