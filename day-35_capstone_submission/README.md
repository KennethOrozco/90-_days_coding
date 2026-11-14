# ML CAPSTONE PROJECT

Compare a Logistic Regression model with a Random Forest model and select the best model
for our requierements. For this project I used the Breast Cancer dataset from scikit-learn.
The models where compared using a pipeline for each and on the same cross validation and then compared by their malignant recall. I used malignant recall as the metric because in a medical environment we 
would like to catch as many malignant tumors as possible.

# Installation

python -m pip install -r requirements-lock.txt

# Training

python -m ml_capstone.training.py

# Testing

From project root run: python -m pytest -v

# Outputs

- best_model.joblib
- metadata.json

THIS PROJECT IS FOR EDUCTAIONAL PURPOSES AND MUST NOT 
BE USED FOR CLINICAL DIAGNOSIS OR TREATMENT DECISIONS.


