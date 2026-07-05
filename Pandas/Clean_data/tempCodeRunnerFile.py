
x=df3["Calories"].mode()[0] # the value that appears most frequently.
df3.fillna({"Calories":x},inplace=True)
print(df3)