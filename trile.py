import joblib
import numpy as np

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Example input (update values based on your dataset columns)
# [Rooms, Distance, Bathroom, Landsize, BuildingArea, YearBuilt]
sample_data = np.array([[3, 20, 1, 200, 150, 1980,0]])

# Predict
predicted_price = model.predict(sample_data)
price_in_inr = predicted_price[0] * 55
print(f"🏠 Predicted House Price: ₹{price_in_inr:,.2f}")
