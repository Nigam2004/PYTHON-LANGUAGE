import pandas as pd

df=pd.read_csv("Pandas/Clean_data/domy.csv")
df["Date"]=pd.to_datetime(df["Date"],format="mixed")
df.dropna(subset=["Calories","Date"],inplace=True)

print(df.to_string())

