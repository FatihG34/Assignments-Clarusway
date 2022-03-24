#!/usr/bin/env python
# coding: utf-8

# ```
#  Let's say; you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
# Write a program that 
# 
# Takes the first name from the user and compares it to yours,
# Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
# If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."
# ```

# In[3]:


user_name_pswrd = {"AlexanderG" : "W.g.22#21"}
crrnt_user = input("Please enter your name for password :")
if crrnt_user in user_name_pswrd:
   print("Hello,", crrnt_user +"! The password is :", user_name_pswrd["AlexanderG"])
else:
    print("Hello,", crrnt_user +"! See you later.")

