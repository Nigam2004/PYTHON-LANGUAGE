import pandas as pd
  # Data frame is like a two dimensional array, it arrange the data in table format like row wise or column wise
data={
    "Name":["Nigam","Ram","sam","daam"],
    "age":[20,30,45,23]
}

#load data into a DataFrame object:
Df=pd.DataFrame(data)
print(Df)  
print(Df.shape)  #(4, 2)