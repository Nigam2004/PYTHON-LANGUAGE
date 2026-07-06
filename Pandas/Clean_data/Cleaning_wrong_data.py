import pandas as pd

df=pd.read_csv("Pandas/Clean_data/domy.csv")
# df.loc[row_no, 'column_name'] = value
for x in df.index:
    if df.loc[x,"Duration"] >120:
      df.loc[x,"Duration"]=99
print(df)