from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    flip_y=0.08,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

depths = [1, 2, 3, 4, 5, 7, 10, None]

data = {}
for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)
    data[depth] = {
        "train_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "difference": train_accuracy - test_accuracy,
        "depth": model.get_depth(),
        "number_of_leaves": model.get_n_leaves()
    }

highest_testing_acc = max(data, key=lambda depth:data[depth]["test_accuracy"])
highest_gap = max(data, key=lambda depth:data[depth]["difference"])

print(highest_testing_acc)
print(highest_gap)

for index, depth in enumerate(data):
    letter = chr(65 + index)
    print(f"Model {letter}")
    print(f"Depth: {depth}")
    print(f"Training Accuracy: {data[depth]["train_accuracy"]}")
    print(f"Testing Accuracy: {data[depth]["test_accuracy"]}")
    print(f"Gap: {data[depth]["difference"]}")
    print(f"Actual Depth: {data[depth]["depth"]}")
    print(f"Number of Leaves: {data[depth]["number_of_leaves"]}")


leaf_sizes = [1, 5, 10]

leaf_data = {}
for leaf_size in leaf_sizes:
    model = DecisionTreeClassifier(max_depth=None, min_samples_leaf=leaf_size, random_state=42)
    model.fit(X_train, y_train)
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)
    leaf_data[leaf_size] = {
        "training_accuracy": train_accuracy,
        "testing_accuracy": test_accuracy,
        "depth": model.get_depth(),
        "number_of_leaves": model.get_n_leaves()
    }

print(leaf_data)

for metric in leaf_data[1]:
    print(f"Metric: {metric}")
    print(f"leaf size 1: {leaf_data[1][metric]}")
    print(f"leaf size 5: {leaf_data[5][metric]}")
    print(f"leaf size 10: {leaf_data[10][metric]}")
    



