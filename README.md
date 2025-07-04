
# 🌱 Sowing Success: Crop Prediction from Soil Metrics Using Logistic Regression

This project applies a logistic regression model to predict the most suitable crop based on soil health indicators. The dataset includes soil nutrient levels (N, P, K) and pH, with the goal of recommending an optimal crop for farmers.

## 📁 Dataset
- **File:** `soil_measures.csv`
- **Columns:**
  - `N`: Nitrogen content
  - `P`: Phosphorous content
  - `K`: Potassium content
  - `ph`: pH level of soil
  - `crop`: Optimal crop (target variable)

## ⚙️ Techniques Used
- Data cleaning and preprocessing
- Train-test splitting
- Logistic Regression (multi-class classification)
- Accuracy evaluation and performance metrics
- Feature importance inspection

## 📊 Model Summary
A logistic regression classifier was trained to predict crop type from numeric soil properties. The model performs well in identifying the appropriate crop based on these parameters.

## 🧪 Future Work
- Try tree-based models (Random Forest, XGBoost)
- Add soil moisture and temperature features
- Deploy as a Streamlit app for real-time crop suggestions

## 🙏 Acknowledgement
Special thanks to **SPCAI-PAFIAST** for providing access to this DataCamp learning opportunity.

---
