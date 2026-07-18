#            **Error Handling**
# 200 --> OK
# 400 --> Bad Request
# 500 --> Server Error

from flask import Flask,jsonify,request
import pickle
import numpy as np

app=Flask(__name__)

model=pickle.load(open('__.pkl','rb'))
scaler=pickle.load(open('__.pkl','rb'))# is you used standard scaler

@app.route('/predict',methods=['POST'])
def predict():
    try:
        data=request.get_json()
        if not data:
            return jsonify({'error': 'No data sent'})
        
        features=data.get('features')
        if not features:
            return jsonify({'error':'Feature field required'})
        
        prediction=model.predict([features])[0]
        return jsonify({'prediction':str(prediction)})
    
    except Exception as e:
        return jsonify({'error':str(e)})


# ** Return probability + label - not just 0/1 **

@app.route('/predict', methods=['POST'])
def predict():
    data=request.get_json()
    features=np.array(data['features']).reshpae(1,-1)
    features_scaled=scaler.transform(features)

    label=model.predict(features_scaled)[0]
    proba=model.predict_proba(features_scaled)[0]
    confidence=round(float(proba[label])*100,2)

    result_text = "Diabetic" if label == 1 else "Not Diabetic"

    return jsonify({
        'prediction': result_text,
        'confidence': confidence,
        'label': int(label)
    })
