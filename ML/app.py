from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

model = pickle.load(open('best_model.sav', 'rb'))
label_encoder = LabelEncoder()
ss = StandardScaler()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    state = data['state']
    district = data['district']
    market = data['market']
    commodity = data['commodity']
    min_price = float(data['min_price'])  # Convert to float
    max_price = float(data['max_price'])  # Convert to float

    # Convert categorical data to numerical data using label encoder
    input_data = [[state, district, market, commodity, min_price, max_price]]
    input_data = label_encoder.fit_transform(input_data)

    # Scale the input data using StandardScaler
    input_data_scaled = ss.fit_transform(input_data)
# Make a prediction using the loaded model
    prediction = model.predict(input_data_scaled.reshape(1, -1))[0]

    # Render the prediction on the results page
    return render_template('results.html', prediction=prediction)