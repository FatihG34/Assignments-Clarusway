#!/usr/bin/env python
# coding: utf-8

# ```
# Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.
# 
# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program which returns True if it's a comfortable word or False otherwise.
# ```

# In[2]:


given_w = set(input("Please enter a word : ").lower())
left = set("qazwsxedcrfvtgb")
right = set("yhnujmıköolçpşğiü")
a = bool(left.intersection(given_w))  # given letters uses to write by left-hand fingers
b = bool(right.intersection(given_w))  # given letters uses to write by right-hand fingers
c = a and b  # It gives writeable by left hand and right hand for given word
print("Is The Word you enter comfortable word : ", c)

