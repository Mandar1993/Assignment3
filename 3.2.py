
#Problem Statement 2:
# Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# Solution:
def myfilter(x): 
    return x % 2 != 0 and x % 3 != 0
result = []
for i in range(2, 25):
    if myfilter(i):
        result.append(i)
        print (i)


#Output:10
