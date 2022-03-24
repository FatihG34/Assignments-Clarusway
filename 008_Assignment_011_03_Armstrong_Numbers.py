#!/usr/bin/env python
# coding: utf-8

# ```
#  Find out if a given number is an "Armstrong Number".
# 
# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
# 371 = 33 + 73 + 13;
# 9474 = 94 + 44 + 74 + 44;
# 93084 = 95 + 35 + 05 + 85 + 45.
# 
# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.
# 
# ```

# In[6]:


print("Let's find out which number is the armstrong number !!!")

while True:
    taken_nmbr = input("Please enter a number : ")
    if not taken_nmbr.isdigit():
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    else:
      break
nmbr = int(taken_nmbr)
t = len(taken_nmbr)

arm_nmbr = 0
s = nmbr

while s > 0 :
  q= s %10
  arm_nmbr += q**t
  s = s // 10

if nmbr == arm_nmbr:
  print(arm_nmbr, "is an Armstrong number")
else:
  print(nmbr, "is not an Armstrong number")    

