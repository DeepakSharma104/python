#factorial using function
import math

def function(n):
    if (n==1)or (n==0):
        return 1
    else:
       return n*function(n-1)
print(function(4)) 

    
    