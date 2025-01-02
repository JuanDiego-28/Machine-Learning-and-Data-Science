from flask import Flask, request, jsonify
import joblib
import pandas as pd


# create flask app 
app = Flask(__name__)

# connect post api call --> predict() function 
@app.route("/predict" , methods=[ "POST"])

def predict():

    # GET JSON REQUEST 
    feat_data = request.json

    # CONVERT JSON  to PANDAS DF 
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)

    # PREDICT 
    prediction = list(model.predict())
    
    #RETURN PREDICTION
    return  jsonify({"prediction" : str(prediction)})

# Load the model  and Set up columns name

if __name__ == "__main__": 

    model = joblib.load("final_model.pk1")
    col_names = joblib.load("col_names.pk1")

    app.run(debug=True)
