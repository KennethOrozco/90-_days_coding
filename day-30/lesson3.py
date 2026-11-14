import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.inspection import permutation_importance
#Part A
data = load_breast_cancer(as_frame=True)

X = data.data
y = data.target

X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)

X_validation, X_test, y_validation, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    random_state=42,
    stratify=y_temp
)
# train randfom forest enesemle
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
rf_model.fit(X_train, y_train)
# get validaton accuracy score
rf_validation_predictions = rf_model.predict(X_validation)
rf_validation_acc = accuracy_score(y_validation, rf_validation_predictions)


#Part B
#calculate permutation importance
result = permutation_importance(
    rf_model,
    X_validation,
    y_validation,
    n_repeats=5,
    random_state=42
)
#make a series out of the result and then sort by high to low
df = pd.Series(
    result.importances_mean,
    index=X_validation.columns
)

sorted_df = df.sort_values(ascending=False)

print(sorted_df.head(10))
#get the 5 most important features and train a new rf ensemble.
best_features = sorted_df.head().index.to_list()
best_ft_X_train = X_train[best_features]
best_ft_X_validation = X_validation[best_features]

tuned_rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
tuned_rf_model.fit(best_ft_X_train, y_train)
tuned_validation_predictions = tuned_rf_model.predict(best_ft_X_validation)
tuned_validation_acc =accuracy_score(y_validation, tuned_validation_predictions)

#compare baseline validation accuracy to the tuned ensemble.

print("Baseline acc: ", rf_validation_acc)

print("Tuned acc: ", tuned_validation_acc)

