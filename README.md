# 🌾 Crop Yield Prediction App  

An AI-powered **Crop Yield Prediction Web App** built with **Streamlit** that helps farmers, students, and researchers estimate crop yield based on soil and weather parameters.  

The app uses a **Random Forest model** trained on agricultural data with features such as Fertilizer usage, Temperature, and Soil nutrients (N, P, K).  

---

## 🚀 Features  
- 📊 Predicts **crop yield** based on user inputs.  
- 🧮 Uses a **trained machine learning model** (Random Forest).  
- 🌱 Sidebar sliders for **easy input of soil and weather parameters**.  
- 🎨 Interactive UI with charts and heatmaps for insights.  
- 📂 Displays dataset samples and visualizations.  
- 🔍 Shows **feature importance** (which factors impact yield the most).  

---

## 🏗️ Project Structure  

📦 CropYieldPrediction
┣ 📜 app.py # Streamlit main app
┣ 📜 model.pkl # Trained ML model (Random Forest)
┣ 📜 scaler.pkl # Scaler fitted on training data
┣ 📜 columns.pkl # Saved feature column names
┣ 📜 crop_yield_dataset.csv # Dataset used for insights
┣ 📜 crop.jpg # Optional image for UI header
┣ 📜 README.md # Project documentation

---

## 📊 Input Parameters

🧪 Fertilizer – amount applied (kg/ha).
🌿 Nitrogen (N) – nitrogen content in soil.
🌱 Phosphorus (P) – phosphorus content in soil.
🍂 Potassium (K) – potassium content in soil.
🌡️ Temperature (°C) – average temperature during growing season.

---

## 🎯 Output

Predicted Crop Yield (units).
Recommendations based on yield level.
Correlation heatmap of dataset.
Scatter plots for Temperature vs Yield and Fertilizer vs Yield.
Feature importance chart.

---

## 🧠 Model Training

Models tested:
Linear Regression
Decision Tree Regressor
Random Forest Regressor ✅ (Best: RMSE ≈ 0.095, R² ≈ 0.99)

---

## 📊 Results
Model	              MAE     	RMSE	     R²
Linear Regression	0.2951	   0.3569	   0.8716
Decision Tree	    0.0789	   0.1225	   0.9849
Random Forest	    0.0624	   0.0949	   0.9909

---

## 🛠️ Tech Stack

Python
Pandas, NumPy, Scikit-learn
Streamlit (for deployment)
Matplotlib / Seaborn (for visualization)

---

## 📷 Output

<img width="1470" height="833" alt="Screenshot 2025-09-14 at 11 31 59 AM" src="https://github.com/user-attachments/assets/6c41a92d-54f3-42d0-9239-a6b21e653a71" />
<img width="1470" height="830" alt="Screenshot 2025-09-14 at 11 32 14 AM" src="https://github.com/user-attachments/assets/28f8b528-6ea9-4420-937a-5ae57924b440" />
<img width="1470" height="831" alt="Screenshot 2025-09-14 at 11 32 24 AM" src="https://github.com/user-attachments/assets/158ea3cd-fb35-452e-ab01-f29398787ffc" />
<img width="1470" height="831" alt="Screenshot 2025-09-14 at 11 34 21 AM" src="https://github.com/user-attachments/assets/325e23a3-f6ed-4b53-9010-8928d6ce8970" />
<img width="1470" height="830" alt="Screenshot 2025-09-14 at 11 34 30 AM" src="https://github.com/user-attachments/assets/c66b12e4-3d14-48e0-a6ba-e02113e97360" />

