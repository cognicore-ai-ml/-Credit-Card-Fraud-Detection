# -Credit-Card-Fraud-Detection
💳 Credit Card Fraud Detection 🔍  
A machine learning project using Python to detect fraudulent credit card transactions. Demonstrates handling imbalanced data, training models like Random Forest and XGBoost, and deploying a Streamlit app for real‑time fraud prediction.  

# 💳 Credit Card Fraud Detection 🔍

## 📌 Overview
This project applies **Machine Learning with Python** to detect fraudulent credit card transactions.  
It demonstrates how to handle **imbalanced datasets**, train models like **Random Forest**, **Logistic Regression**, and **XGBoost**, and evaluate them using **Precision**, **Recall**, **F1-score**, and **ROC-AUC** metrics.  
A simple **Streamlit app** is included to allow users to upload transaction data and get real-time fraud predictions.

---

## 📊 Dataset
Dataset: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
⚠️ Note: The dataset is not included in this repository due to size and licensing restrictions. Please download it directly from Kaggle and place it in the `data/` folder.

---

## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection
pip install -r requirements.txt

streamlit run app/app.py

---

▶️ Usage
Run the Streamlit app to test fraud detection interactively:
`bash
streamlit run app/app.py
`
Upload a CSV file containing transaction data to get real-time fraud predictions.

---

📈 Results
- Random Forest achieved the best balance between precision and recall.  
- ROC-AUC score showed strong discrimination between fraudulent and non-fraudulent transactions.  
- The Streamlit app provides an easy way to visualize predictions.

---

🚀 Future Improvements
- Integrate deep learning models (LSTM for sequential data).  
- Deploy on AWS, Azure, or Heroku for public access.  
- Add SHAP explainability to interpret model decisions.  
- Implement real-time streaming detection for live transactions.

---

👨‍💻 Author
Developed by Mohammed  
Diploma in Machine Learning with Python
