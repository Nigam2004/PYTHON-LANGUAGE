import pandas as pd

df=pd.read_csv("Pandas/Clean_data/domy.csv")
print(df.duplicated())
print(df.drop_duplicates(inplace=True))
# The drop_duplicates(inplace=True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
# # To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row: