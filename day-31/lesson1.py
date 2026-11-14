from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Part A

#Organize data as features and targets.
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
#make a model using pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])
# Train model
model.fit(X_train, y_train)
#Predict on test data
predictions = model.predict(X_test)
#Calculate and print test accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy score: ", accuracy)

#Part B

#retrieve scaler
scaler = model.named_steps["scaler"]

#print the training mean for each feature and the scale factor used for each feature
print(scaler.mean_)
print(scaler.scale_)

#retrieve the classifier
classifier = model.named_steps["classifier"]
#print classifier coefficient shape
print(classifier.coef_.shape)

#Part C

#make unscaled model
unscaled_model = LogisticRegression(max_iter=1000)
#Train model on the same training data
unscaled_model.fit(X_train, y_train)
#get predicitons
unscaled_predictions = unscaled_model.predict(X_test)
#Calculate accuracy
unscaled_accuracy = accuracy_score(y_test, unscaled_predictions)

#Print comparison with pipeline model using a scaler and the unscaled model
print("Scaled accuracy: ", accuracy)
print("Unscaled accuracy: ", unscaled_accuracy)