# %% [markdown]
# ```
# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
# 
# The examples of the desired output are as follows :
# 
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number
# 
# ```

# %%
digit1 = input("Enter a number : ")
while not digit1.isdigit():
    print("You must enter the number you entered as digits")
    digit1 = int(input("Enter a number : "))
    break
dgt = int(digit1)
if (dgt == 1) or (dgt == 0) :
    print("The number", dgt, "is not a prime number. The smallest prime number is considered to be 2.")
else:
    for i in range(2,dgt):
        if (dgt % i != 0) and (dgt > 1):
            print("Hello, the number you entered is ", digit1, "and that is prime number.")
        else:
            print("Opppss, the number you entered is ", digit1, "and that is not prime number")
        break


