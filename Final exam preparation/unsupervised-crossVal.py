from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import KFold
import numpy as np

# Load dataset
data = load_iris()
X = data.data

# Use 5-fold split (unsupervised: no y)
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)

silhouette_scores = []

for fold, (train_index, test_index) in enumerate(kf.split(X), 1):
    X_train, X_test = X[train_index], X[test_index]

    # Train KMeans on train split
    model = KMeans(n_clusters=3, n_init=10, random_state=42)
    model.fit(X_train)

    # Predict clusters for test split
    labels = model.predict(X_test)

    # Evaluate using silhouette score
    score = silhouette_score(X_test, labels)
    silhouette_scores.append(score)
    print(f"Fold {fold} Silhouette Score: {score:.4f}")

# Average performance
mean_score = np.mean(silhouette_scores)
print(f"\nMean Silhouette Score over {k} folds: {mean_score:.4f}")

#Silhouette Score measures how well points fit in their clusters: 
#Score ranges from -1 (bad) to +1 (ideal)
#Values > 0.5 indicate good separation
#Though unsupervised, cross-validation style runs help assess model consistency
