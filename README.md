# diabetes_mlops_production
# 🏥 HealthPredict: End-to-End MLOps Pipeline & Diabetes Analysis.

> **Bridging the gap between Machine Learning research and production using MLflow, Docker, and Railway.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🌟 Executive Summary

**HealthPredict** is a sophisticated MLOps-driven application designed to provide real-time diabetes disease progression analysis. 

By integrating **MLflow** for experiment tracking and **Docker** for containerization, this project moves beyond simple model training into a full production lifecycle. The system interprets clinical data (Age, BMI, Blood Pressure) through a calibrated Random Forest model, providing users with immediate health risk assessments and data-driven insights.

## 🚀 Key Features

* **🔄 Automated Experiment Tracking:** Uses **MLflow** to log hyperparameters, performance metrics, and model versions during every training run.
* **🐳 Containerized Architecture:** Encapsulated using **Docker**, ensuring the application runs identically on any machine or cloud provider.
* **📊 Interactive Analytics Dashboard:** A high-performance **Streamlit** interface that handles raw user inputs and provides visual distribution charts.
* **⚖️ Smart Data Pre-processing:** Includes an automated scaling layer that converts standard user inputs (like real age) into model-ready normalized features.
* **☁️ Cloud-Native Deployment:** Pre-configured for **Railway** deployment with automatic CI/CD and public URL generation.

## 📊 Performance Metrics

The model is evaluated based on the standard Scikit-Learn Diabetes dataset metrics, tracked and logged via MLflow:

| Metric | Action Performed |
| :--- | :--- |
| **Mean Squared Error** | 📉 Tracks the average squared difference between estimated values and the actual value. |
| **R² Score** | 📈 Indicates the proportion of the variance in the dependent variable that is predictable. |
| **Model Registry** | 📦 Versions the best-performing model for seamless production deployment. |

## 🛠️ System Architecture

The application operates on a modern 3-tier MLOps structure:
1.  **Training Phase (`train.py`):** Trains the model and pushes serialized artifacts and metrics to the **MLflow** tracking server.
2.  **Preprocessing Phase:** Converts "Normal User" inputs into scaled mathematical features.
3.  **Deployment Phase:** Wraps the **Streamlit** frontend and model in a **Docker** container for hosting on **Railway**.



## ScreenShot:

<img width="1919" height="1079" alt="MLOps Project Screenshot" src="https://github.com/user-attachments/assets/b04576c9-6338-4834-acdd-dc88b7e29668" />


## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/shankarin2k6/diabetes_mlops_production.git](https://github.com/shankarin2k6/diabetes_mlops_production.git)
cd diabetes_mlops_production
```
### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install streamlit pandas numpy plotly mlflow scikit-learn
```
### 3. Execution Commands
To run the project locally, follow these steps in order:

Step 1: Train and Log via MLflow
```bash
python train.py
```
Step 2: Launch the Dashboard
```bash
streamlit run app.py
```

Thank You for visiting!!!
By Shankari N
