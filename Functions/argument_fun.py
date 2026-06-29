def add(*number):
    print(number)
    total=0
    for n in number:
        total+=n   
    return total
    
print(add(1,2,3))

"""Explantion=> On the above funcion *number act as tuplee ,all the argument are stored in form of tupple and user can perform any action related tuple """