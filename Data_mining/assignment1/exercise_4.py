import pandas as pd
#1.1
# df = pd.DataFrame({
#     'Feature1':[2, 3, 4, 5],
#     'Feature2':[10, 20, 30, 40]
# })

# df['Result'] = df['Feature1'] * df['Feature2']

# print(df)

# #1.2
# from sklearn.preprocessing import PolynomialFeatures

# df = pd.DataFrame({
#     'Feature1':[1, 2, 3],
#     'Feature2':[4, 5, 6]
# })

# poly = PolynomialFeatures(degree=2, include_bias = False)
# new_features = poly.fit_transform(df)

# """
# Признак1 = 1
# Признак2 = 4
# Признак1^2 = 1^2 = 1
# Признак1 * Признак2 = 1 * 4 = 4
# Признак2^2 = 4^2 = 16
# """

# print(new_features)

# -----------------------------------------------------------

# #2
# df = pd.DataFrame({
#     'Date' : ['2023-01-01', '2023-05-15', '2024-07-20']
# })

# df['Date'] = pd.to_datetime(df['Date'])

# # Извлечение года, месяца и дня
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day

# print(df)

# -----------------------------------------------------------

#3
df = pd.DataFrame({
    'Time' : ['08:30', '14:45', '18:20', '22:10']
})

df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

def time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 22:
        return 'Evening'
    else:
        return 'Night'

df['Time_hour'] = df['Time'].apply(lambda x:time_of_day(x.hour))

print(df)