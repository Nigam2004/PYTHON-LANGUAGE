import pandas as pd

json_data=pd.read_json("Pandas/fundamental/JSON DATA.json")

print(json_data)


##dictiobary can diretly load   into dataframe(JSON = Python Dictionary

student={
    "name":["nigam","ram","dam","sam"],
    "roll_no":20,
    "age":21,
    "mark":85

}
df=pd.DataFrame(student)
print(df)
