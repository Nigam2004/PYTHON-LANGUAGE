childrens={}
childrens["name"]="Jeon"
childrens["age"]=25 
childrens["gender"]="m" 
childrens["father_name"]="Ram" 
childrens["mother_name"]="Urmila" 
print(childrens.pop("name"))

"""ans -Jeon"""

student={
    "name":["nigam","ram","dam","sam"],
    "roll_no":20,
    "age":21,
    "mark":85

}

print(student["name"][1])
"""ans -ram"""
print(student.keys())
"""dict_keys(['name', 'roll_no', 'age', 'mark'])"""