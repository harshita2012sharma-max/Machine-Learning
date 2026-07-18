"""
QUESTION-1 What is Rest API and Flask?
ANSWER     Rest Api is a set of URLs (called endpoints) that your frontend can call to send or recieve the request.
-----      And Flask is a framework that lets you craete the URLS in python .

-----      HTML FORM (Fetch()) --> Flask route ---> python logic  ---> Json response

"""

# Install flask and its helpers
# pip install flask flask-cors

""" 
Why flask-cors? 
Your HTML file runs on port 5500 (Live Server), Flask runs on 5000. Browsers 
block cross-origin requests by default — CORS removes that block.
"""

# For ML project add these too
#pip install scikit-learn numpy pandas mysql-connector-python pickle5

from flask import Flask,request,jsonify
# from flask_cors import CORS 

app=Flask(__name__)  
# __name__ tells Flask where your file is
# CORS(app)
# allows all origin for dev

# @app.route="when user visits /url,run this function"
# methods=which HTTP verb are allowed

@app.route('/hello',methods=['GET'])
def Hello():
    return jsonify({"msg":"Hello"})

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json() # get json body from frontend
    age=data['age']
    result=age*2
    return jsonify({'result':result})

if __name__=="__main__":
    app.run(debug=True,port=5000) # auto restart on save

"""
HTTP methos -->

1. GET 
Read data.No bosy ,Used for fetching history,getting lists.

2. POST
Send data + create.Has body(Json).Used for predictions,login,signup

3. PUT
Update existing record.Has body with new values

4. DELETE
Delete record .Usually ID passed in URL.
"""

# // GET request — no body needed
# const res = await fetch('http://localhost:5000/history');
# const data = await res.json();

# // POST request — send JSON body
# const res = await fetch('http://localhost:5000/predict', {
#   method: 'POST',
#   headers: { 'Content-Type': 'application/json' },
#   body: JSON.stringify({ age: 25, glucose: 148 })
# });
# const result = await res.json();
# document.getElementById('output').textContent = result.prediction;