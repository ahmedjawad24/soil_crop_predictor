# 🌱 Soil Crop Predictor

A machine learning-based web application that predicts the most suitable crop for cultivation based on soil features using a regression model.

Built with Python, Scikit-learn, and Streamlit, this project demonstrates how regression models can guide agricultural decisions using real-world soil data.

---

## 🚀 Features

- 🌾 Predicts optimal crop from soil data (N, P, K, pH, temperature, etc.)
- 🧠 Trained using **Random Forest Regression**
- 🎛️ Frontend built with **Streamlit** for instant interaction
- 📦 Includes serialized model and label encoder
- 🧪 Notebook for EDA, preprocessing, and model training

---

## 📁 Project Structure

| File/Folder                      | Description                                       |
|----------------------------------|---------------------------------------------------|
| `app.py`                         | Streamlit web app script                          |
| `soil_crop_prediction.ipynb`     | Jupyter notebook for data processing and modeling |
| `soil_measures_separated_large.csv` | Input dataset                                  |
| `requirements.txt`              | Python dependencies                               |


---

## 📊 Input Features

- **Nitrogen (N)**
- **Phosphorus (P)**
- **Potassium (K)**
- **Temperature**
- **Humidity**
- **pH**
- **Rainfall**

---

## 🧪 Model Used

- Random Forest Regression
- MAE, MSE, R² metrics used for evaluation
- LabelEncoder used to convert regression outputs to crop names

---

## ⚙️ Installation & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/ahmedjawad24/soil_crop_predictor.git
   cd soil_crop_predictor
