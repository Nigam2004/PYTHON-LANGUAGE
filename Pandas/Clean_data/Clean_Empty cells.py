import pandas as pd


#Clean empty cell using dropna()  ------------------------------------
df1=pd.read_csv("Pandas/Clean data/domy.csv")
print(df1)
new_df=df1.dropna()  
## through this dropna() method it remove all the row which cell is NULL without affecting original dataframe
print(new_df)

df1.dropna(inplace=True)
## through this dropna(inplace=True) method it remove all the row which cell is NULL from  original dataframe
print(df1)

#Clean empty cell using fillna()------------------------------------
df2=pd.read_csv("Pandas/Clean data/domy.csv")
df2.fillna({"Calories": 130,"Date": 140}, inplace=True)
## through fillna(142,inplace=True) method  it replace  all the NULL value with 142
print(df2)



##Clean empty cell using mean()------------------------------------
df3=pd.read_csv("Pandas/Clean data/domy.csv")
x=df3["Calories"].mean() # the average value (the sum of all values divided by number of values).
df3.fillna({"Calories":x},inplace=True)
print(df3)

##Clean empty cell using median()------------------------------------
df4=pd.read_csv("Pandas/Clean data/domy.csv")
x=df4["Calories"].median() # the value in the middle, after you have sorted all values ascending.
df4.fillna({"Calories":x},inplace=True)
print(df4.to_string())


##Clean empty cell usingmode()[0]------------------------------------
df5=pd.read_csv("Pandas/Clean data/domy.csv")
x=df5["Calories"].mode()[0] # the value that appears most frequently.
df5.fillna({"Calories":x},inplace=True)
print(df5)

