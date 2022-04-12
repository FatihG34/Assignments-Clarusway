# %% [markdown]
# ```
# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.
# 
# The desired output is like this:
# 
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 
# ```

# %%
fbn_nmbr = int(input("Please enter positive integer numbers : "))
fb = [1]
n1, n2 = 0, 1
for i in range(fbn_nmbr+1):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    fb.append(n2)
print("The first {} Fibonacci numbers are below".format(fbn_nmbr + 2))
print("This is Fibonacci Numbers : ", fb)

# %%



