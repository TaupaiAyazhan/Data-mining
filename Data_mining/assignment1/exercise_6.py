import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    'Feature1' : [1, 2, 3, 4, 5],
    'Feature2' : [10, 20, 30, 40, 50],
    'Target' : [0, 1, 0, 1, 0]
})

# axis=1 removing a COLUMN from the DataFrame
# axis=0: removing a ROW from the DataFrame

X = df.drop('Target', axis=1) 
y = df['Target']

# print(df) #all
# print(X)  #feature1 and feature2
# print(y)  #only target

#70-30
X_train_70, X_test_30, y_train_70, y_test_30 = train_test_split(X, y, test_size=0.3, random_state=42)

#80-20
X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()

model.fit(X_train_70, y_train_70)
predictions_70 = model.predict(X_test_30)
accuracy_70 = accuracy_score(y_test_30, predictions_70)

model.fit(X_train_80, y_train_80)
predictions_80 = model.predict(X_test_20)
accuracy_80 = accuracy_score(y_test_20, predictions_80)

print(f"Accuracy with 70-30 split: {accuracy_70:.2f}")
print(f"Accuracy with 80-20 split: {accuracy_80:.2f}")