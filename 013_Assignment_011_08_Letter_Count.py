#!/usr/bin/env python
# coding: utf-8

# In[25]:


given_sntc = input("Please enter a sentence : ")

let_dict = {}

for i in given_sntc:
    
    let_dict[i] = given_sntc.count(i)


print()
print(let_dict)

