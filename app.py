import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# ------------------ Load Model & Preprocessors ------------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")  # should NOT contain 'yield'

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="🌾 Crop Yield Prediction",
    page_icon="🌱",
    layout="wide"
)

# ------------------ Header Section ------------------
st.title("🌾 Crop Yield Prediction App")
st.markdown(
    """
    Welcome to the **AI-powered Crop Yield Predictor**!  
    Enter soil and weather details to estimate the crop yield 🌱🚜
    """
)

# Add a header image
try:
    image = Image.open("crop.jpg")
    st.image(image, caption="Healthy Crops 🌿")
except:
    st.info("💡 Tip: Add a `crop.jpg` image in the project folder to display here.")

# ------------------ Sidebar for Inputs ------------------
st.sidebar.header("🧑‍🌾 Enter Soil & Weather Parameters")

fertilizer = st.sidebar.slider("🧪 Fertilizer", 0, 200, 80, help="Amount of fertilizer applied")
nitrogen = st.sidebar.slider("🌿 Nitrogen (N)", 0, 200, 50, help="Low <40 | Medium 40-80 | High >80")
phosphorus = st.sidebar.slider("🌱 Phosphorus (P)", 0, 100, 30, help="Low <20 | Medium 20-50 | High >50")
potassium = st.sidebar.slider("🍂 Potassium (K)", 0, 150, 40, help="Low <40 | Medium 40-100 | High >100")
temperature = st.sidebar.slider("🌡️ Temperature (°C)", 5, 50, 25, help="Ideal 15-30°C")

# Build input DataFrame with column names SAME as training
input_df = pd.DataFrame([[fertilizer, temperature, nitrogen, phosphorus, potassium]],
                        columns=["Fertilizer", "temp", "N", "P", "K"])


# ------------------ Prediction Section ------------------
st.subheader("🔍 Prediction Results")

if st.button("🚀 Predict Yield"):
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)
    
    st.success(f"🌱 Estimated Crop Yield: **{prediction[0]:.2f} units**")
    st.balloons()  
    st.progress(100)  

    # ------------------ Recommendations ------------------
    st.subheader("📊 Insights & Recommendations")

    if prediction[0] < 2:
        st.warning("⚠️ Low yield expected. Consider increasing **fertilizer (N, P, K)** or improving irrigation 💧.")
    elif 2 <= prediction[0] < 4:
        st.info("🙂 Moderate yield. Try optimizing sowing time and ensuring proper pest management 🐛.")
    else:
        st.success("🎉 High yield expected! Maintain current practices for best results 🌟.")

    # ------------------ Dataset & Visualizations ------------------
    st.subheader("📂 Dataset Insights")
    try:
        dataset = pd.read_csv("crop_yield_dataset.csv")  # <-- place your dataset in same folder
        st.dataframe(dataset.head(10))  # Show first 10 rows

        # --- Correlation Heatmap ---
        st.write("### 🔥 Correlation Heatmap")
        plt.figure(figsize=(8, 5))
        sns.heatmap(dataset.corr(), annot=True, cmap="YlGnBu")
        st.pyplot(plt)


        # --- Temperature vs Yield ---
        st.write("### 🌡️ Temperature vs Yield")
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=dataset["temp"], y=dataset["yeild"])
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Yield")
        st.pyplot(plt)

    except:
        st.info("⚠️ Add `crop_data.csv` in project folder to unlock full visualizations.")

    # ------------------ Feature Importance ------------------
    st.subheader("🌟 Feature Importance (Factors affecting yield)")
    try:
        importances = model.feature_importances_
        feat_imp = pd.DataFrame({"Feature": columns, "Importance": importances})
        feat_imp = feat_imp.sort_values(by="Importance", ascending=False)

        plt.figure(figsize=(8, 5))
        sns.barplot(x="Importance", y="Feature", data=feat_imp, palette="viridis")
        plt.title("Feature Importance from Random Forest")
        st.pyplot(plt)

    except:
        st.error("⚠️ Feature importance not available for this model.")

else:
    st.info("👈 Enter values in the sidebar and click **Predict Yield** to start.")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "✨ Developed with ❤️ using **Streamlit** | Powered by **Random Forest AI Model**"
)
