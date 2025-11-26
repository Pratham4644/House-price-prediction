from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

# Load your model
model = joblib.load("house_price_model.pkl")

@app.route("/")
def home():
    return "🏠 House Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([
            [
                data["Rooms"],
                data["Bathroom"],
                data["Landsize"],
                data["BuildingArea"],
                data["Lattitude"],
                data["Longtitude"],
                data["Propertycount"]
            ]
        ])

        prediction = model.predict(features)[0]

        # Convert AUD to INR (₹) and scale to lakhs
        prediction_in_inr = prediction * 55 / 100000

        return jsonify({
            "predicted_price_lakh": round(prediction_in_inr, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
