# 🧠 Machine Learning-Based Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-orange)

---

# 💳 Machine Learning-Based Fraud Detection System

## 📌 Project Overview
This project presents a machine learning-based fraud detection system designed to identify fraudulent financial transactions using real-world credit card transaction data. The system applies data balancing techniques and multiple classification algorithms to improve detection performance in highly imbalanced datasets.

The solution is built as a deployable AI application using **Streamlit**, making it accessible as an interactive web app.

---

## 👤 Author
**Akpojotor Emmanuel Oghenechovwe**  
Department of Computing  
National Open University of Nigeria (NOUN)  
Email: nou224068313@noun.edu.ng  

---

## 🚀 Live Demo (After Deployment)
👉 HuggingFace Spaces: *(to be added after deployment)*  
👉 GitHub Repository: *(current repo link)*  

---

## 📊 Dataset
The dataset used is the **Credit Card Fraud Detection dataset**, which contains anonymized transaction data from European cardholders.

- Total records: 284,807 transactions  
- Fraud cases: ~0.17% (highly imbalanced dataset)  
- Features: PCA-transformed variables (V1–V28), Amount, Class  

Source:
- Kaggle Credit Card Fraud Dataset

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Standard scaling applied to `Amount`
- Removed `Time` feature (if present)
- Feature separation into X (inputs) and y (target)

### 2. Class Imbalance Handling
- SMOTE (Synthetic Minority Over-sampling Technique)
- Balanced fraud vs non-fraud distribution

### 3. Machine Learning Models
The following models were implemented:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier (Best performing model)

---

## 🧠 Model Training Pipeline

```python
StandardScaler → SMOTE → Train-Test Split → Model Training → Evaluation