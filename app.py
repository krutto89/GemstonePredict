import json
from flask import Flask, render_template, jsonify,request
import pickle
import numpy as np
from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

app = Flask(__name__)

model = pickle.load(open('src/pipeline/artifacts/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method =="GET":
        return render_template('form.html')
    else:
        #Get the data from the form
        data = CustomData(
                          carat=float(request.form.get('carat')),
                          cut=request.form.get('cut'),
                          color=request.form.get('color'),
                          clarity=request.form.get('clarity'),
                          depth=float(request.form.get('depth')),
                          table=float(request.form.get('table')),
                          x=float(request.form.get('x')),
                          y=float(request.form.get('y')),
                          z=float(request.form.get('z')))
        
    final_data = data.get_data_as_dataframe()

    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_data)
    result = round(pred[0],2)

    return render_template('result.html',final_result=result)

    # return render_template('result.html',prediction_text="The price of the Diamond is ${}".format(result))
    


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',port=5000)