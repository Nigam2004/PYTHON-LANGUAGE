# set is not support duplicate value

num=[10,20,30,40,50,50,50,50]
x=set(num)
print(type(x))
y={10,20,30,40,50,50,50,50}
print(y)


a={1,2,3,4,5}
b={4,5,6,9,7}
print(a | b) #set Union
print(a & b) #set intersection
print(a - b) #set diffrence
