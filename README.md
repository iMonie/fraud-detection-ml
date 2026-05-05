

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-orange)

---
# 💳 Fraud Detection AI

An end-to-end machine learning application that detects fraudulent credit card transactions in real-time using a trained Random Forest model.

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/Akpoj/fraud-detection-ai  

Try the app by entering transaction features (V1–V28) and Amount to predict whether a transaction is fraudulent.

---

## 🧠 Problem Statement

Credit card fraud is a highly imbalanced classification problem where fraudulent transactions are extremely rare but costly.

This project builds a robust ML pipeline to accurately detect fraud while minimizing false negatives.

---

## ⚙️ Solution Overview

- Built and compared multiple models:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
- Applied **SMOTE** to handle class imbalance  
- Selected **Random Forest** for best overall performance  
- Deployed using an interactive web interface  

---

## 📊 Model Performance

| Model                | Accuracy | Notes |
|---------------------|---------|------|
| Logistic Regression | 97%     | High recall |
| Random Forest       | ~99.9%  | Best balance |
| XGBoost             | ~98.7%  | High recall |

> Focus was on maximizing fraud detection (recall) while maintaining precision.

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- XGBoost  
- Imbalanced-learn (SMOTE)  
- Gradio (UI)  
- Hugging Face Spaces (Deployment)  
- GitHub (Version Control)  

---

## ⚡ Features

- ✅ Real-time fraud prediction  
- 📊 Probability/confidence score  
- 🎨 Color-coded results (Fraud / Not Fraud)  
- 🧪 Interactive testing interface  
- 🔁 Consistent preprocessing using saved scaler  

---

## 🧩 How It Works

1. User inputs transaction features  
2. Amount is scaled using saved StandardScaler  
3. Model predicts fraud or not fraud  
4. Probability scores are generated  
5. Results displayed instantly via UI  

---

## 📁 Project Structure


app.py
requirements.txt
fraud_model.pkl
scaler.pkl
README.md


---

## ⚠️ Notes

- Dataset: anonymized credit card transactions  
- Model files may be excluded from GitHub due to size limits  
- Use the live demo for full functionality  

---

## 🚀 Future Improvements

- 🔍 SHAP explainability  
- 📈 Fraud analytics dashboard  
- 🌐 FastAPI backend  
- 🔐 Authentication system  

---

## 👤 Author

**Akpojotor Emmanuel Oghenechovwe**  
Department of Computing  
National Open University of Nigeria (NOUN)  
📧 Email: nou224068313@noun.edu.ng  

---

## 🔗 Project Links

👉 **Hugging Face App:**  
https://huggingface.co/spaces/Akpoj/fraud-detection-ai  

👉 **GitHub Repository (Notebook):**  
https://github.com/iMonie/fraud-detection-ml/blob/main/fraud-detection-ml-project.ipynb  

👉 **Full GitHub Repository:**  
https://github.com/iMonie/fraud-detection-ml  

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐


