import pandas as pd
# -----------------------------------------------------------------------------
#1
# data = {
#     'Name': ['John', 'Anna', 'John', 'Mike', 'Anna'],
#     'Age': [28, 22, 28, 35, 22],
#     'City': ['New York', 'London', 'New York', 'Paris', 'London']
# }

# df = pd.DataFrame(data)

# # print(df.info())
# print(df.duplicated())
# df_cleaned = df.drop_duplicates()
# print(df_cleaned)
# -----------------------------------------------------------------------------

#2
# data = {
#     'Name': ['John', 'Anna', 'Mike', 'Lisa', 'Peter'],
#     'Age': [28, 22, 35, 120, 25],
# }

# df = pd.DataFrame(data)

# Q1 = df['Age'].quantile(0.25)
# Q3 = df['Age'].quantile(0.75)
# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# df_no_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

# print(df_no_outliers)

# -----------------------------------------------------------------------------

3
data = {
    'Name': ['John', 'john', 'Anna', 'ANNA', 'Mike'],
    'City': ['New York', 'new york', 'London', 'london', 'PARIS']
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].str.lower().str.title()
df['City'] = df['City'].str.title()

print(df)