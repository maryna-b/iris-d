# app.py
import pickle
from flask import Flask, request, jsonify

# Load the saved model C:/Users/Marina/
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the simple ML model API!"

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = model.predict([data]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)