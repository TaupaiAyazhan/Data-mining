import pandas as pd
df = pd.read_csv('Apple_price_to_clean.csv')

# print(df.isnull().sum()) #determining the amount of missing data
# df_cleaned = df.dropna() #Removing rows with missing values

# fillna() method allows you to fill in missing values
# df['Date'].fillna(df['Date'].mean(), inplace=True)  #column's mean value
# df['Date'].fillna(df['Date'].median(), inplace=True) #column's median value

data = {'Date': ['2022-01-01', None, '2023-01-01', '', '2024-02-01']}
df = pd.DataFrame(data)     
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# df['Date'] = df['Date'].fillna(pd.Timestamp('2024-01-01'))  #column's specific meaning value
print(df)

# df['Date'].ffill(inplace=True) #to fill the gaps with the previous value
df['Date'].bfill(inplace=True) #to fill the gaps with the next value
print(df)