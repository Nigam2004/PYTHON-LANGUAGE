# String

word="nigam" #Indexing- [n,i,g,a,m]=[0,1,2,3,4]=[0,-4,-3,-2,-1]
print(word[1])
print(word[-4])
"""ans-
i
i"""


#string[start:end]
# end-not included
# ex=5 5-1=4
#Slicing

print(word[0:4])
"""ans-niga
"""
print(word[:3])
"""ans-nig
"""
print(word[2:])
"""ans-gam
"""
#string[start:end:step]  
# end-not included
# step-how much step will skip after 0 ,if it is 2 then it skip 2-1=1 , means it will skip 1 step after 0
# ex=5 5-1=4

print(word[0:5:2])
"""ans-ngm
"""
print(word[::-1])
"""ans-magin
"""