from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('flight_rf.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Dep_Time = request.form['Dep_Time']
        Journey_day = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").month)
              
        Dep_Time_hrs = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").hour)
        Dep_Time_min = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").minute)
                       
        Arrival_Time = request.form['Arrival_Time']
        Arrival_Time_hrs = int(pd.to_datetime(Arrival_Time, format="%Y-%m-%dT%H:%M").hour)
        Arrival_Time_min = int(pd.to_datetime(Arrival_Time, format="%Y-%m-%dT%H:%M").minute)
                           
        Duration_hours = abs( Arrival_Time_hrs - Dep_Time_hrs ) 
        Duration_minute = abs( Arrival_Time_min - Dep_Time_min ) 
                           
        Total_Stops = int(request.form['Total_Stops'])
                          
        Airline = request.form['Airline']
        if(Airline=="Jet Airways"):
                      Jet_Airways = 1
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
        
        elif(Airline=="IndiGo"):
                      Jet_Airways = 0
                      IndiGo = 1
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
                      
        elif(Airline=="Air India"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 1
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
                    
        elif(Airline=="Multiple carriers"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 1
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
                      
        elif(Airline=="SpiceJet"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 1
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
            
        elif(Airline=="Vistara"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 1
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
                      
        elif(Airline=="GoAir"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 1
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0

        elif(Airline=="Jet Airways Business"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 1
                      Vistara_Premium_economy = 0
                      Trujet = 0
                      
        elif(Airline=="Vistara Premium economy"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 1
                      Trujet = 0
                      
        elif(Airline=="Trujet"):
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 1
        
        else:
                      Jet_Airways = 0
                      IndiGo = 0
                      Air_India = 0
                      Multiple_carriers = 0
                      SpiceJet = 0
                      Vistara = 0
                      GoAir = 0
                      Multiple_carriers_Premium_economy = 0
                      Jet_Airways_Business = 0
                      Vistara_Premium_economy = 0
                      Trujet = 0
                      
                      
        Source = request.form["Source"]
        if (Source == 'Chennai'):
                      Chennai = 1
                      Delhi = 0
                      Kolkata = 0
                      Mumbai = 0
        elif (Source == 'Delhi'):
                      Chennai = 0
                      Delhi = 1
                      Kolkata = 0
                      Mumbai = 0
        elif (Source == 'Kolkata'):
                      Chennai = 0
                      Delhi = 0
                      Kolkata = 1
                      Mumbai = 0
        elif (Source == 'Mumbai'):
                      Chennai = 0
                      Delhi = 0
                      Kolkata = 0
                      Mumbai = 1
        else :
                      Chennai = 0
                      Delhi = 0
                      Kolkata = 0
                      Mumbai = 0
                      
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
                      Cochin = 1
                      Delhi = 0
                      Hyderabad = 0
                      Kolkata = 0
                      New_Delhi = 0
        elif (Destination == 'Delhi'):
                      Cochin = 0
                      Delhi = 1
                      Hyderabad = 0
                      Kolkata = 0
                      New_Delhi = 0
        elif (Destination == 'Hyderabad'):
                      Cochin = 0
                      Delhi = 0
                      Hyderabad = 1
                      Kolkata = 0
                      New_Delhi = 0
        elif (Destination == 'Kolkata'):
                      Cochin = 0
                      Delhi = 0
                      Hyderabad = 0
                      Kolkata = 1
                      New_Delhi = 0
        elif (Destination == 'New Delhi'):
                      Cochin = 0
                      Delhi = 0
                      Hyderabad = 0
                      Kolkata = 0
                      New_Delhi = 1
        else :
                      Cochin = 0
                      Delhi = 0
                      Hyderabad = 0
                      Kolkata = 0
                      New_Delhi = 0
                      
        prediction = model.predict([[Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy, Chennai, Delhi,
       Kolkata, Mumbai, Cochin, Delhi, Hyderabad, Kolkata,
       New_Delhi, Total_Stops,Journey_day, Journey_month,
       Dep_Time_hrs, Dep_Time_min, Arrival_Time_hrs, Arrival_Time_min,
       Duration_hours, Duration_minute]])
              
        output=round(prediction[0],2)
        if output<=0:
            return render_template('index.html',prediction_texts="Please enter correct information")
        else:
            return render_template('index.html',prediction_texts=f"Price = {output}")
    
        
        
    else:
        return render_template('index.html')

    
    
#if __name__=="__main__":
#    app.run(debug=True)  
if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
        
