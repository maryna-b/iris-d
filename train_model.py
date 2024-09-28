# train_model.py
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset (iris)
data = load_iris()
X, y = data.data, data.target

# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the model to a file using pickle
with open('/model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")