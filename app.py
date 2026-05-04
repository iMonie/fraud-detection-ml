import gradio as gr
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

def predict(*inputs):
    data = np.array(inputs).reshape(1, -1)
    pred = model.predict(data)[0]
    
    if pred == 1:
        return "🚨 FRAUD DETECTED"
    else:
        return "✅ LEGITIMATE TRANSACTION"

# Create 29 inputs (V1–V28 + Amount)
inputs = [gr.Number(label=f"V{i}") for i in range(1, 29)]
inputs.append(gr.Number(label="Amount"))

app = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs="text",
    title="💳 Fraud Detection AI",
    description="Enter transaction details to predict fraud"
)

app.launch()