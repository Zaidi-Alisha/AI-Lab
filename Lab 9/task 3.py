import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('customers.csv')
data.head()

#cleaning dataset
data = data.dropna()
print("Missing values: ", data.isnull().sum())
data.dropna(inplace=True)

#remove extreme outliers (you can adjust this)
for col in ['TotalSpending6Months', 'NumVisits', 'PurchaseFreq']:
    q_low = data[col].quantile(0.01)
    q_hi  = data[col].quantile(0.99)
    data = data[(data[col] > q_low) & (data[col] < q_hi)]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# feature Scaling
features = ['Age', 'TotalSpending6Months', 'NumVisits', 'PurchaseFreq']
X = data[features]
y = data['CustomerID']  # target variable (0 or 1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print(f"\nAccuracy Score: {accuracy_score(y_test, y_pred):.4f}")
