from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

data = load_breast_cancer(as_frame=True)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#Build Logistic Regression Pipeline and Random Forest Tree pipeline

lr_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000))
])

rf_pipeline = Pipeline([
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

#Perform cross-validaton useing StratifiedKFold

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

lr_scores = cross_val_score(
    lr_pipeline,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)

rf_scores = cross_val_score(
    rf_pipeline,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy"
)
#Print scores for both models

print("Logistic Regression accuracy scores: ", lr_scores)
print("Random Forest Classifier accuracy scores: ", rf_scores)

#Summarize the results
lr_mean = lr_scores.mean()
lr_std = lr_scores.std()
lr_range = lr_scores.max() - lr_scores.min()

rf_mean = rf_scores.mean()
rf_std = rf_scores.std()
rf_range = rf_scores.max() - rf_scores.min()

print("Logistic Regression's mean: ", lr_mean)
print("Logistic Regression's standard deviaton: ", lr_std)
print("Logistic Regression's range: ", lr_range)

print("Random Forest's mean: ", rf_mean)
print("Random Forest's standard deviation: ", rf_std)
print("Random Forests range: ", rf_range)

if sum(lr_scores) > sum(rf_scores):
    print("Logistic Regression model is better!")
elif sum(rf_scores) > sum(lr_scores):
    print("Random Forest Classifier is better!")
else:
    print("They perform around the same.")