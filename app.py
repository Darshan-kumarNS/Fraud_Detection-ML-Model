from flask import Flask, render_template, request
import joblib,pickle
import numpy as np
import pandas as pd

# Load the Random Forest model
model=joblib.load(open('random.pkl','rb'))

from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    payment_method = (request.form['payment_method'])
    partner_id = (request.form['partner_id'])
    partner_category = (request.form['partner_category'])
    device_type = (request.form['device_type'])
    money_transacted = (request.form['money_transacted'])
    partner_pricing_category = (request.form['partner_pricing_category'])


    data = [[payment_method, partner_id, partner_category, device_type, money_transacted, partner_pricing_category]]
    prediction = model.predict(data)

    prediction = model.predict(data)
    if prediction == 0:
        return render_template('index.html', prediction_text='This is not a Fraud Transaction')

    else:
        return render_template('index.html', prediction_text='Careful! This might be a Fraud Transaction')


if __name__ == "__main__":
    app.run(debug=True)