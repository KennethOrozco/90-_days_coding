import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Part A

customers = pd.DataFrame({
    "age": [
        25, 34, np.nan, 42, 29, 51,
        38, np.nan, 45, 31, 27, 49
    ],
    "annual_income": [
        45000, np.nan, 72000, 95000,
        58000, 110000, 67000, 52000,
        np.nan, 61000, 48000, 105000
    ],
    "membership": [
        "Basic", "Premium", "Basic",
        None, "Standard", "Premium",
        "Standard", "Basic", "Premium",
        "Standard", None, "Premium"
    ],
    "region": [
        "North", "South", "East",
        "West", "North", "South",
        "East", "West", "North",
        "South", "East", "West"
    ],
    "purchased": [
        0, 1, 0, 1, 0, 1,
        1, 0, 1, 0, 0, 1
    ]
})
#replace missing values of None with nan
customers = customers.replace({None:np.nan})
#Seperate feautres into X and y

X = customers[["age", "annual_income", "membership", "region"]]

y = customers["purchased"]

#Split data set into train and test.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
#Define two list

numerical_features = ["age", "annual_income"]
categorical_features = ["membership", "region"]

#Part B

#Build numerical pipeline
numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

#Build categorical pipeline
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    ))
])

# Create ColumnTransformer using both pipelines

preprocessor = ColumnTransformer([
    ("numeric", numerical_pipeline, numerical_features),
    ("categorical", categorical_pipeline, categorical_features)
])

#Create final pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

#Train Pipeline on train data
model.fit(X_train, y_train)
#Get the predictions
predictions = model.predict(X_test)
#Get test accracy and print
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)

#Part D

#fitted preprocessor
fitted_preprocessor = model.named_steps["preprocessor"]

#Transform training features using preprocessor
X_train_transformed = fitted_preprocessor.transform(X_train)

#Print the original shape and th transformed shape
print("Original shape: ", X_train.shape)
print("Transformed shape: ", X_train_transformed.shape)

#Get feature names and print them
feature_names = fitted_preprocessor.get_feature_names_out()

print(feature_names)






