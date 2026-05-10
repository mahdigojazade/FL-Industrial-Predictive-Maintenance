# FL Industrial Predictive Maintenance

A Federated Learning-based predictive maintenance system for industrial equipment using the NASA Turbofan Engine Degradation Simulation Dataset.

---

## Project Overview

This project implements a Federated Learning (FL) framework for predictive maintenance in industrial environments.

The goal is to predict equipment degradation and potential failures using distributed machine learning without sharing raw sensor data between clients.

The project uses the NASA CMAPSS turbofan engine dataset and simulates multiple FL clients for decentralized training.

---

## Features

- Federated Learning simulation
- Industrial predictive maintenance
- Distributed client training
- Global model aggregation (FedAvg)
- Data preprocessing and normalization
- Model evaluation metrics
- PyTorch-based neural network

---

## Technologies Used

- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

## Dataset

NASA Turbofan Engine Degradation Simulation Dataset (CMAPSS)

Dataset used:
- FD001 subset

---

## Project Structure

FL_Industrial_Project/

data/
train_FD001.txt

notebooks/
فناوری.ipynb

src/
preprocessing.py
model.py
train.py
federated.py
evaluation.py

requirements.txt
README.md

---

## Federated Learning Workflow

1. Data preprocessing
2. Client data partitioning
3. Local client training
4. Federated averaging (FedAvg)
5. Global model aggregation
6. Evaluation and prediction

---

## Model Performance

Current experimental results:

- Accuracy: 96%
- Precision: 85%
- Recall: 91%
- F1 Score: 88%

---

## Installation

pip install -r requirements.txt

---

## Run Project

python train.py

---

## Future Improvements

- Real-time industrial dashboard
- Flower framework integration
- Edge-device deployment
- Real federated communication
- Streamlit visualization dashboard

---

## Author

Mahdi Gojazade

Computer Engineering Student
Federated Learning Researcher