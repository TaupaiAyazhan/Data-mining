#1
# from sklearn.preprocessing import MinMaxScaler
# import pandas as pd

# df = pd.DataFrame({
#     'column': [1, 2, 3, 4, 5]
# })

# scaler = MinMaxScaler()
# df[['column']] = scaler.fit_transform(df[['column']])
# print(df)

# -----------------------------------------------------------------------------

#2
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# df = pd.DataFrame({
#     'Category': ['A', 'B', 'A', 'C'],
#     'Value': [10, 20, 10, 30]
# })

# # df_dummies = pd.get_dummies(df, columns=['Category']) #converts the 'Category' column into multiple columns of 0 and 1, where each column represents a category.
# # print(df_dummies)

# encoder = OneHotEncoder(sparse_output=False)
# encoded = encoder.fit_transform(df[['Category']])

# # Create a new DataFrame with encoded data
# df_encoded = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Category']))

# # Merge the encoded data with the original DataFrame
# df_final = pd.concat([df.drop('Category', axis=1), df_encoded], axis=1)
# print(df_final)

# -----------------------------------------------------------------------------
#3

import pandas as pd

df = pd.DataFrame({
    'Value': [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
})
bins = [0, 30, 60, 100]

labels = ['Low', 'Medium', 'High']

df['Value_Grouped'] = pd.cut(df['Value'], bins=bins, labels=labels)
print(df)