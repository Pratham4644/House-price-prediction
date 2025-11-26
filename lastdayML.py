import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load the cleaned data
df = pd.read_csv(r"C:\Users\bs529\OneDrive\Desktop\ML(Kaggle)\data\melb_data.csv")


# Fill missing values (same as before)
df.fillna({
    'Car': df['Car'].median(),
    'BuildingArea': df['BuildingArea'].median(),
    'YearBuilt': df['YearBuilt'].median(),
    'CouncilArea': 'Unknown'
}, inplace=True)

# Select features (independent variables)
features = ['Rooms', 'Distance', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt']

# Target variable (dependent)
target = 'Price'

# Define X (inputs) and y (output)
X = df[features]
y = df[target]

# Split data into training and testing (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model Trained Successfully!")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.3f}")

# Save the model
joblib.dump(model, 'house_price_model.pkl')
print("💾 Model saved as 'house_price_model.pkl'")
