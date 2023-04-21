from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# load the model
model = pickle.load(open('best_model.sav', 'rb'))

# define the home page
@app.route('/')
def home():
    return render_template('index.html')

# define the results page
@app.route('/predict', methods=['POST'])
def predict():
    # get the form inputs
    market = request.form['market']
    commodity = request.form['commodity']
    variety = request.form['variety']
    grade = request.form['grade']

    # load the dataset
    data = pd.read_excel("Date-Wise-Prices-all-Commodity.xlsx")
    # filter the dataset based on market, commodity, and variety
    filtered_data = data[(data['Market'] == market) & (data['Commodity'] == commodity) & (data['Variety'] == variety)]
    
    min_price = float(filtered_data['Min_x0020_Price'].iloc[0])
    max_price = float(filtered_data['Max_x0020_Price'].iloc[0])

    # preprocess the inputs
    label_encoder=LabelEncoder()
    ss=StandardScaler()
    market_encoded = label_encoder.fit_transform([market])
    commodity_encoded = label_encoder.fit_transform([commodity])
    variety_encoded = label_encoder.fit_transform([variety])
    grade_encoded = label_encoder.fit_transform([grade])
    data = np.array([market_encoded[0], commodity_encoded[0], variety_encoded[0], grade_encoded[0], min_price, max_price]).reshape(1, -1)
    data = ss.fit_transform(data)
    
    # make the prediction
    prediction = model.predict(data)
    
    # round the prediction to two decimal places
    prediction = round(prediction[0], 2)
    
    # render the results page with the prediction
    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
