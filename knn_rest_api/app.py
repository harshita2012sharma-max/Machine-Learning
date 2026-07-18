from flask import Flask, request, jsonify
import pandas as pd
import pickle

app=Flask(__name__)

with open("knn.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_dict = {
        "age": data["age"],
        "gender": data["gender"],
        "fever": data["fever"],
        "cough": data["cough"],
        "city": data["city"]
    }

    df = pd.DataFrame([input_dict])
    prediction = model.predict(df)

    return jsonify({
        "prediction": prediction[0]
    })


if __name__ == "__main__":
    app.run(debug=True)



