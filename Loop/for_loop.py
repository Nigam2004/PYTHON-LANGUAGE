roll_no=[1,2,3,4,5]
for i in roll_no:
    print("nigam:",i)

"""it prints 
nigam: 1
nigam: 2
nigam: 3
nigam: 4
nigam: 5"""

roll_no=[1,2,3,4,5]
for i in roll_no:
     if i==4:
          break
     print(i)

"""It prints 1,2,3"""



for i in range(6):
    i+=1
    print(i)

"""it prints
1
2
3
4
5
6"""


for i in range(6,0,-1):
    print(i)

"""It prints 
6
5
4
3
2
1"""

for i in range(6,0,-1):
    if i==3:
        continue
    print(i)
"""it prints-
6
5
4
2
1"""

for i in range(6,0,-1):
    if i==3:
        pass
    print(i)
# pass dones nothing
"""it print 
6
5
4
3
2
1"""


     
