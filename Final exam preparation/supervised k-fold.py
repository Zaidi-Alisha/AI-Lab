from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Initialize k-Fold Cross Validation
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)

accuracies = []

# Loop over folds
for fold, (train_index, test_index) in enumerate(kf.split(X), 1):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Train logistic regression model
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

    print(f"Fold {fold} Accuracy: {acc:.4f}")

# Overall performance
mean_accuracy = np.mean(accuracies)
print(f"\nMean Accuracy over {k} folds: {mean_accuracy:.4f}")

Fold 1 Accuracy: 0.9649
Fold 2 Accuracy: 0.9298
Fold 3 Accuracy: 0.9649
Fold 4 Accuracy: 0.9561
Fold 5 Accuracy: 0.9737

Mean Accuracy over 5 folds: 0.9579
