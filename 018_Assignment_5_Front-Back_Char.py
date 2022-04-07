#!/usr/bin/env python
# coding: utf-8

# ```
# Given a string, return a new string where the first and last chars have been exchanged.
# For example:
# 
# Test             	                 Result
# print(front_back('clarusway'))       ylaruswac
# print(front_back('a'))               a
# print(front_back('ab'))              ba
# 
# ```

# In[27]:


def front_back(word):
    a_list = list(word)
   
    if len(a_list) > 1:
        first_itemoflist = a_list[0]
        a_list[0] = a_list[-1]
        a_list[-1] = first_itemoflist
        front_back = "".join(a_list)
        return front_back
    else:
        return word


# In[28]:


front_back("a")


# In[31]:


front_back("how is woh")


# In[32]:


front_back("how is wow")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




