# ♻️ Waste Classification ML App

This project is an end-to-end machine learning solution for classifying waste into categories like glass, metal, plastic, cardboard, and more. It combines deep learning with modern deployment tools to create an interactive and scalable system.

## 🔍 Overview

The system uses **MobileNetV2**, a lightweight and efficient CNN architecture, fine-tuned for waste classification. It supports:

- **Flask API** for serving predictions programmatically
- **Streamlit Web App** for user-friendly image upload and prediction
- **TensorFlow/Keras** for model training and evaluation
- **Image preprocessing and validation tools** to clean and organize datasets
- **sklearn** for evaluation metrics like classification report and confusion matrix

The project covers the entire pipeline from data cleaning and model training to deployment and user interaction.

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- Flask
- Streamlit
- scikit-learn
- PIL (Pillow)
- NumPy
- OS / shutil for data handling

## 🏁 Features

- Train a custom waste classifier using transfer learning
- Clean and validate datasets before training
- Serve model via REST API using Flask
- Provide live predictions via Streamlit interface
- Evaluate model accuracy with real-world test data
