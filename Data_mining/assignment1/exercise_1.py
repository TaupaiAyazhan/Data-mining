import pandas as pd
df = pd.read_csv('Apple_price_to_clean.csv')

print(df.head()) #first five
print(df.tail()) #last five
print(df.info()) # dataset, data types, number non-null, memory usage
print(df.isnull()) #True for null, False for non-null
print(df.dtypes) #data type of each column