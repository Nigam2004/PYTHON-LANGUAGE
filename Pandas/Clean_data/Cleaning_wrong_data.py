import pandas as pd

df=pd.read_csv("Pandas/Clean_data/domy.csv")
# df.loc[row_no, 'column_name'] = value
print(df.loc[1,"Duration"])
for x in df.index:
    if df.loc[x,"Duration"] >120:
      df.loc[x,"Duration"]=99
print(df)