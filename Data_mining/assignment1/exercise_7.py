import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    'Feature1': [1, 2, None, 4, 5],
    'Feature2': ['A', 'B', 'A', 'B', 'C'], 
    'Target': [0, 1, 0, 1, 0]
})

X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = ['Feature1']
categorical_features = ['Feature2']

numeric_pipeline = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy = 'mean')), # Filling missing values ​​with mean
    ('scaler', StandardScaler())                    # Scaling of numerical features
])

categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), # Filling in missing values ​​with the most frequent
    ('onehot', OneHotEncoder(handle_unknown='ignore'))   # Coding of categorical features
])

# Merging pipelines into one
preprocessor = ColumnTransformer(
    transformers = [
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ]
)
#Building a Full Pipeline: Combine the preprocessing pipeline with a machine learning model.
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression()) # Machine learning model
])

#Train the model: Fit the pipeline to the training data.
model_pipeline.fit(X_train, y_train)

# Prediction and Model Evaluation: Transform the test data and perform prediction.
predictions = model_pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")