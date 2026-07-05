import pandas as pd

# The head(--rows--) method returns the headers and a specified number of rows, starting from the top.

csv_data=pd.read_csv("Pandas/fundamental/EPF APR CRYSTAL.csv")
print(csv_data.head(10)) 
 #if rows mentioned then it wil return the 10 rows from starting.
 
print(csv_data.head())  
#if rows not mentioned then it wil return by default 5 rows from starting.


# The tail(--rows--) method returns the headers and a specified number of rows, starting from the bottom.

print(csv_data.tail(10))
 #if rows mentioned then it wil return the 10 rows from bottom.

print(csv_data.tail())
 #if rows not mentioned then it wil return by default 5 rows from bottom.
