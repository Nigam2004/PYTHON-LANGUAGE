def s_detail(name,age,gender):
    print("name:",name,"age:",age,"gender:",gender)
s_detail("nigam",20,"m")
# ans->name: nigam age: 20 gender: m

s_detail(20,"m","nigam")
# ans->name: 20 age: m gender: nigam ,
# explanation=>in this ans we can observe that the name,age,gender argument are given but the place of the approprite value are missmatch that's why we use key-word-argument.

s_detail(age=20,name="Sneha",gender="F")
# ans=>name: Sneha age: 20 gender: F


