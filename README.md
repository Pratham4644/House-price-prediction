# 🏡 House Price Prediction

A machine learning project that predicts house prices based on various features such as rooms, bathroom count, land size, building area, location coordinates, and more.
This project includes data preprocessing, model training, evaluation, and deployment using a Flask API.

---

## 📌 Project Structure

```
├── data/
│   └── melb_data.csv
├── model/
│   ├── model.pkl
│   └── scaler.pkl
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

---

## 🚀 Features

* Data cleaning and preprocessing
* Handling missing values
* Feature engineering
* Model training using Regression Algorithms
* Model evaluation with metrics
* API deployment with Flask
* Frontend integration (optional)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pratham4644/House-price-prediction.git
cd House-price-prediction
```

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

Run the training script:

```bash
python train.py
```

This will generate:

* `model.pkl`
* `scaler.pkl`

---

## 🌐 API Usage

### Run Flask Server:

```bash
python app.py
```

### Example API Request:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"Rooms":2,"Bathroom":1,"Landsize":150,"BuildingArea":150,"Lattitude":-37.8,"Longtitude":144.9,"Propertycount":1}'
```

---

## 🛠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-Learn
* Flask
* Git & GitHub
* VS Code

---

## 📈 Results

* Achieved good accuracy using regression models.
* Model performance metrics can be added here after evaluation.

---

## 🙌 Author

**Prathamesh Shinde**
GitHub: [https://github.com/Pratham4644](https://github.com/Pratham4644)

---

## 📝 License

This project is open-source and available under the MIT License.
