# Federated Learning for Industrial Predictive Maintenance

## Abstract

This project presents a Federated Learning (FL) approach for predictive maintenance in industrial systems using the NASA CMAPSS turbofan engine dataset.

The system aims to predict equipment degradation and potential failures while preserving data privacy by avoiding centralized raw data sharing.

A distributed learning architecture was implemented using multiple simulated clients and a global aggregation strategy based on Federated Averaging (FedAvg).

Experimental results demonstrate that the proposed approach can achieve high predictive performance while maintaining decentralized training capabilities.

---

## Introduction

Industrial predictive maintenance has become one of the most important applications of Artificial Intelligence in modern industries.

Traditional machine learning systems require centralized data collection, which may introduce privacy risks, communication overhead, and security concerns.

Federated Learning provides a decentralized solution where multiple clients collaboratively train a shared global model without transferring raw sensor data.

This project investigates the application of Federated Learning in predictive maintenance scenarios using sensor-based industrial datasets.

---

## Objectives

- Develop a Federated Learning framework
- Simulate distributed industrial clients
- Predict equipment degradation
- Preserve data privacy
- Evaluate model performance

---

## Dataset

The NASA CMAPSS Turbofan Engine Degradation Simulation Dataset was used in this project.

Dataset subset:
- FD001

The dataset contains:
- Sensor measurements
- Operational settings
- Engine degradation trajectories

---

## Methodology

### Data Preprocessing

- Feature selection
- Data normalization
- Label generation
- Client data partitioning

### Federated Learning Process

1. Local client training
2. Weight extraction
3. Federated Averaging (FedAvg)
4. Global model aggregation
5. Performance evaluation

### Model Architecture

A neural network model was implemented using PyTorch.

The model was trained locally on multiple simulated clients before global aggregation.

---

## Experimental Results

Current experimental results:

- Accuracy: 96%
- Precision: 85%
- Recall: 91%
- F1 Score: 88%

These results demonstrate the effectiveness of Federated Learning for industrial predictive maintenance applications.

---

## Technologies Used

- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Git
- GitHub

---

## Future Improvements

Future development directions include:

- Real-time federated communication
- Flower framework integration
- Industrial dashboard development
- Edge-device deployment
- Real-time anomaly detection
- Streamlit-based visualization system

---

## Conclusion

This project demonstrates the feasibility of applying Federated Learning to industrial predictive maintenance systems.

The proposed framework enables collaborative machine learning while preserving data privacy and reducing centralized data dependency.

The project can serve as a foundation for future industrial AI systems and real-world federated learning applications.

---

## Author

Mahdi Gojazade

Computer Engineering Student  
Federated Learning Researcher