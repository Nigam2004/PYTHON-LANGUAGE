# lambda is used to create a small, anonymous function in a single line without using the def keyword.
import pandas as pd
#Example using def
def add(x):
    print("norma:",x+x)
add(5)
#returns: norma: 10

#using lambda 
add=lambda x:x+x
print("lambda:",add(5)) 
#returns: lambda: 10


#using list
nums=[10,20,30]
mult=list(map(lambda x:x*2,nums))
print(mult)
