#!/usr/bin/env python
# coding: utf-8

# ```
#  Task : Estimating the risk of death from coronavirus. Write a program that;
# 
# Takes "Yes" or "No" from the user as an answer to the following questions :
# 
# Are you a cigarette addict older than 75 years old? Variable → age
# 
# Do you have a severe chronic disease? Variable → chronic
# 
# Is your immune system too weak? Variable → immune
# 
# Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).
# ```

# In[4]:


age = input("Are you a cigarette addict older than 75 years old?: " ).title() 
chronic = input("Do you have a severe chronic disease? : " ).title()
immune = input("Is your immune system too weak? : " ).title()
if age == "Yes" or chronic == "Yes" or immune == "Yes" :
  print("You are in risky group")
else:
  print("You are not in risky group")

