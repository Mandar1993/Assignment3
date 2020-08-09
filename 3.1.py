#Problem Statement 1:
# Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
#Solution :
def myreduce(l):
    s = 0
    for i in l:
        s = s + i
    return s
j=myreduce([1,2,3,4,])
print(j)


#Output:10
