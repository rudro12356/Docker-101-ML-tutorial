from flask import Flask, request, jsonify
import numpy as np
import pickle
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
app = Flask(__name__)

# Load the trained model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['input'])])
    output = prediction[0]
    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)