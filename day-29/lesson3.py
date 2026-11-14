from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Store train, test accuracy, and generalization gap from depth values in a dictionary
def experiment_depth(depth_values: list[int | None]) -> list[dict[str, int | float | None]]:
    rf_data = []
    for depth in depth_values:
        rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=depth,
            random_state=42
        )
        rf_model.fit(X_train, y_train)
        train_predictions = rf_model.predict(X_train)
        test_predictions = rf_model.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_predictions)
        test_accuracy = accuracy_score(y_test, test_predictions)
        generalizaton_gap = train_accuracy - test_accuracy
        dictionary = {
            "max_depth": depth,
            "train_accuracy": train_accuracy,
            "test_accuracy": test_accuracy,
            "generalization_gap": generalizaton_gap,
        }
        rf_data.append(dictionary)
    return rf_data

#Store train, test accuracy, and generalization gap from esimator values in a dictionary
def experiment_estimators(estimator_values:list[int]) -> list[dict[str, float]]:
    rf_data = []
    for estimators in estimator_values:
        rf_model = RandomForestClassifier(
            n_estimators=estimators,
            max_depth=5,
            random_state=42
        )
        rf_model.fit(X_train, y_train)
        train_predictions = rf_model.predict(X_train)
        test_predictions = rf_model.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_predictions)
        test_accuracy = accuracy_score(y_test, test_predictions)
        generalizaton_gap = train_accuracy - test_accuracy
        dictionary = {
            "n_estimators": estimators,
            "train_accuracy": train_accuracy,
            "test_accuracy": test_accuracy,
            "generalization_gap": generalizaton_gap,
        }
        rf_data.append(dictionary)
    return rf_data

#Store train, test accuracy, and generalization gap from leaf values in a dictionary
def experiment_leaf(leaf_values):    
    rf_data = []
    for leaf in leaf_values:
        rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            min_samples_leaf=leaf,
            random_state=42,
        )
        rf_model.fit(X_train, y_train)
        train_predictions = rf_model.predict(X_train)
        test_predictions = rf_model.predict(X_test)
        train_accuracy = accuracy_score(y_train, train_predictions)
        test_accuracy = accuracy_score(y_test, test_predictions)
        generalizaton_gap = train_accuracy - test_accuracy
        dictionary = {
            "min_samples_leaf": leaf,
            "train_accuracy": train_accuracy,
            "test_accuracy": test_accuracy,
            "generalization_gap": generalizaton_gap,
        }
        rf_data.append(dictionary)
    return rf_data




data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

depth_values = [2, 3, 5, 8, 12, None]

estimator_values = [5, 10, 25, 50, 100, 200]

leaf_values = [1, 2, 4, 8, 16]

rf_depth_data = experiment_depth(depth_values)

rf_estimator_data = experiment_estimators(estimator_values)

rf_leaf_data = experiment_leaf(leaf_values)

#identify the highest test accuracy for the depth configuration
max_test_acc_depth = max(depth["test_accuracy"] for depth in rf_depth_data)
print(max_test_acc_depth)
highest_depth_models = [tree["max_depth"] for tree in rf_depth_data if tree["test_accuracy"] == max_test_acc_depth]
print("Depth Values: ", highest_depth_models)

#identify the highest test accuracy for the estimator configuration
max_test_acc_est = max(estimators["test_accuracy"] for estimators in rf_estimator_data)
print(max_test_acc_est)
highest_estimators_models = [tree["n_estimators"] for tree in rf_estimator_data if tree["test_accuracy"] == max_test_acc_est]
print("Estimator Values: ", highest_estimators_models)

#identify the highest test accuracy for the min samples leaf configuration
max_test_acc_leaf = max(leaf["test_accuracy"] for leaf in rf_leaf_data)
print(max_test_acc_leaf)
highest_leaf_models = [tree["min_samples_leaf"] for tree in rf_leaf_data if tree["test_accuracy"] == max_test_acc_leaf]
print("Leaf Values: ", highest_leaf_models)

#get smallest gap from configurations
min_gap_depth = min(tree["generalization_gap"] for tree in rf_depth_data)
min_gap_est = min(tree["generalization_gap"] for tree in rf_estimator_data)
min_gap_leaf = min(tree["generalization_gap"] for tree in rf_leaf_data)

print("depth gap: ", min_gap_depth)
print("estimator gap: ", min_gap_est)
print("leaf gap: ", min_gap_leaf)

lowest_depth_gap_models = [tree["max_depth"] for tree in rf_depth_data if tree["generalization_gap"] == min_gap_depth]
print("Depth Values for gap: ", lowest_depth_gap_models)