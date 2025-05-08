import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv('email.csv')

data.head()

data = data.dropna()
#seeing the type of no binary values are given and then converting it to binary
print("Unique values in the email data set: ", data['Category'].unique())

binary_columns = ['Category']
#converting it to 1/0
data[binary_columns] = data[binary_columns].apply(lambda x : x.map({'ham': 0, 'spam' : 1}))
#printing the updated unique values
print("Updated Unique Values: ", data['Category'].unique())

import seaborn as sns
#training the model to classify emials
# Split into training and testing sets
data = data[['Category', 'Message']].dropna()
X_train, X_test, y_train, y_test = train_test_split(data['Message'], data['Category'], test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

new_email = ["URGENT: Your account has been compromised, click here to reset"]
new_tfidf = vectorizer.transform(new_email)
prediction = model.predict(new_tfidf)[0]
print("New Email Prediction:", "Spam" if prediction == 1 else "Ham")
