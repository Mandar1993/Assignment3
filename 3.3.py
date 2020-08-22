#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2. Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#1.['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
l= ['x','y','z']
result = [item * num for item in l for num in range(1,5)]
result


# In[2]:


#2.['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
l = ['x','y','z']
res = [num * i for num in range(1,5) for i in l]
res


# In[3]:


#3.[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
l = [2,3,4]
res = [[num + i] for i in l for num in range(0,3)]
res


# In[4]:


#4.[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
l = [2,3,4,5]
res = [[num+i for i in l] for num in range(0,4)]
res


# In[5]:


#5.[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

l = [1,2,3]
res = [(b,a) for b in l for a in l]
res


# In[ ]:




