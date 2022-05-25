#!/usr/bin/env python
# coding: utf-8

# `` Your task is to sum the differences between consecutive pairs in the array in descending order.[2, 1, 10]  -->  9
# In descending order: [10, 2, 1]
# 
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
# 
# If the array is empty or the array has only one element the result should be 0(Nothing in Haskell).
# ```

# In[7]:


new_list = [11, 2, 1, 9, 5, 7]
srt = sorted(new_list, reverse = True)
srt


# In[24]:


def sumof_list(a_list):
    summ = 0
    sorted_list = sorted(a_list, reverse = True)
    for i in range((len(a_list)-1)):
        summ += sorted_list[i] - sorted_list[i+1]
        yield summ


# In[25]:


yaz = list(sumof_list(new_list))
yaz

