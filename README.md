# 🧠 ANN-Based Customer Churn Classification

This project implements a deep learning model (Artificial Neural Network) using TensorFlow and Keras to predict customer churn based on various demographic and account-related features.

The model is deployed as an interactive web app using **Streamlit**. You can try the live app [here](https://ann-customerchurn-classification-arjunverma2004.streamlit.app/) _(if running)_.

---

## 🚀 Demo

![App Screenshot](https://github.com/arjunverma2004/ANN-CustomerChurn-classification/blob/main/screenshots/Screenshot.png)

> Predict whether a customer will churn or not using a trained neural network.

---

## 📂 Project Structure

ANN-CustomerChurn-classification/

│

├── app.py     #Streamlit app frontend

├── model/     #Saved model (.h5 file)

├── dataset/ #Original customer churn dataset

├── requirements.txt #Python dependencies

├── runtime.txt #Python version for deployment

├── README.md #Project documentation (you're reading it!)


---

## 📊 Dataset

- The dataset is sourced from [Telco Customer Churn dataset](https://www.kaggle.com/blastchar/telco-customer-churn) and contains customer information such as:
  - Gender
  - SeniorCitizen
  - Tenure
  - MonthlyCharges
  - Contract type
  - Internet service, etc.

- Target: `Churn` (Yes/No)

---

## 🧠 Model

- Framework: **TensorFlow + Keras**
- Architecture:
  - Input layer with 11 features
  - 2 hidden layers with ReLU activation
  - Output layer with sigmoid activation
- Binary classification output (Churn: Yes/No)

---

## 💻 Installation

### 📦 Clone the repository

```bash
git clone https://github.com/arjunverma2004/ANN-CustomerChurn-classification.git
cd ANN-CustomerChurn-classification
```

## 🐍 Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Streamlit App Locally

```bash
streamlit run app.py
```

## ✍️ Author

**Arjun Verma**

- GitHub: [@arjunverma2004](https://github.com/arjunverma2004)  
- LinkedIn: [Arjun Verma](https://www.linkedin.com/in/arjunverma2004/)
