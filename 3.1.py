#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem Statement 2:
# Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# Solution:
def f(x): 
    return x % 2 != 0 and x % 3 != 0
result = []
for i in range(2, 25):
    if f(i):
        result.append(i)
        print (i)


# In[ ]:




