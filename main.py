from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('gradient_boost_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_2.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Car_Name_i20 = request.form['Car_Name']
        if(Car_Name_i20=='i20'):
                Car_Name_i20=1
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='innova'):
                Car_Name_i20=0
                Car_Name_innova=1
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='innova'):
                Car_Name_i20=0
                Car_Name_innova=1
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='verna'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=1
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='brio'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=1
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='ciaz'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=1
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='city'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=1
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='corolla altis'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=1
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i20=='fortuner'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=1
                Car_Name_i10=0
                Car_Name_other=0
                Car_Name_grand_i10=0
        elif(Car_Name_i10=='i10'):
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=1
                Car_Name_other=0
                Car_Name_grand_i10=0
        else:
                Car_Name_i20=0
                Car_Name_innova=0
                Car_Name_verna=0
                Car_Name_brio=0
                Car_Name_ciaz=0
                Car_Name_city=0
                Car_Name_corolla_altis=0
                Car_Name_fortuner=0
                Car_Name_i10=0
                Car_Name_other=1
                Car_Name_grand_i10=0
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        Year=2020-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven2,Year,Car_Name_brio,Car_Name_ciaz,Car_Name_city,Car_Name_corolla_altis,Car_Name_fortuner,
Car_Name_grand_i10,Car_Name_i20,Car_Name_innova,Car_Name_other,Car_Name_verna,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index_2.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index_2.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index_2.html')

if __name__=="__main__":
    app.run(debug=True)

