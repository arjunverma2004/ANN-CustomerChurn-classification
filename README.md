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

### 📊 Dataset

The dataset is sourced from the [**Bank Customer Churn Dataset**](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset), which contains information about customers of a bank and whether they have churned (i.e., closed their account).

It includes features such as:

- **CustomerId** – Unique ID for each customer  
- **Surname** – Customer’s last name  
- **CreditScore** – Credit score of the customer  
- **Geography** – Country of residence  
- **Gender** – Male or Female  
- **Age** – Customer’s age  
- **Tenure** – Number of years as a customer  
- **Balance** – Account balance  
- **NumOfProducts** – Number of bank products held  
- **HasCrCard** – Whether the customer has a credit card (1 = Yes, 0 = No)  
- **IsActiveMember** – Whether the customer is an active member  
- **EstimatedSalary** – Estimated annual salary  
- **Exited** – **Target variable** indicating churn (1 = Yes, 0 = No)

This dataset is suitable for building classification models to predict whether a customer will leave the bank.

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
