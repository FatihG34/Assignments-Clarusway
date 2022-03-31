#!/usr/bin/env python
# coding: utf-8

# ```
# Given a non-empty string and an int n, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in the original string (i.e. n will be in the range 0....len(str)-1 inclusive).
# 
# For example:
# 
# Test                                                  Result
# 
# print(missing_char('kitchen', 1))                     ktchen
# 
# print(missing_char('kitchen', 0))                     itchen
# 
# print(missing_char('kitchen', 4))                     kitcen
# ```

# In[29]:


def missing_char(word, n):
    a_list = list(word)
    a_list[n] = ""
    word2 = "".join(a_list)
    return word2


# In[30]:


missing_char('kitchen', 1)


# In[31]:


missing_char('olacak', 1)


# In[32]:


missing_char('olacak', 1)


# In[13]:


def missing_char(word, n):
    a_list = list(word)
    a_list.pop(n)
    word2 = "".join(a_list)
    return word2


# In[14]:


missing_char('kitchen', 1)


# In[15]:


def missing_char(word, n):
    a_list = list(word)
    del a_list[n]
    word2 = "".join(a_list)
    return word2


# In[16]:


missing_char('kitchen', 1)


# In[17]:


def missing_char(word, n):
    a_list = list(word)
    a_list.remove(a_list[n])
    word2 = "".join(a_list)
    return word2


# In[18]:


missing_char('kitchen', 1)


# In[ ]:




