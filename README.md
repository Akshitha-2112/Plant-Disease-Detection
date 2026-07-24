# 🌿 Plant Disease Detection Using Deep Learning

## 📌 Overview

Plant Disease Detection is a deep learning-based web application that detects diseases in plant leaves from uploaded images. The application uses a Convolutional Neural Network (CNN) model to classify plant diseases and provides the predicted disease along with recommended remedies. The project aims to help farmers and agricultural professionals identify plant diseases early and reduce crop losses.

---

## 🚀 Features

- Upload plant leaf images through a user-friendly web interface.
- Detect plant diseases using a trained CNN model.
- Display the predicted disease name.
- Provide disease information and recommended remedies.
- Fast and accurate image classification.
- Simple Flask-based web application.

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend
- Python
- Flask

### Deep Learning
- TensorFlow
- Keras
- Convolutional Neural Network (CNN)

### Libraries
- NumPy
- OpenCV
- Pillow
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure

```
Plant-Disease-Detection/
│
├── dataset/
├── image/
├── database/
├── buildmodel.py
├── training_cnn.py
├── training_vgg16.py
├── imagepreprocessing.py
├── algorithmperformance.py
├── knnaccuracy.py
├── svm_accuracy.py
├── plantdiseasedetection.py
├── login.py
├── adminhome.py
├── home.py
├── dbconn.py
├── graph.py
├── *.h5
├── *.pkl
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## 🧠 Model Workflow

1. Collect and preprocess plant leaf images.
2. Resize and normalize images.
3. Train a CNN model using the processed dataset.
4. Save the trained model.
5. User uploads a leaf image through the Flask application.
6. The image is preprocessed.
7. The CNN model predicts the disease.
8. The application displays the predicted disease and recommendations.

---

## 📊 Image Preprocessing

- Image resizing
- Pixel normalization
- Label encoding
- Data augmentation
- Dataset splitting for training and testing

---

## 📈 Model Performance

The CNN model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The model achieved high classification accuracy on the testing dataset.

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Plant-Disease-Detection.git
```

### Navigate to the project

```bash
cd Plant-Disease-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python plantdiseasedetection.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📷 Screenshots

Add screenshots of:

- Home Page
- Login Page
- Image Upload Page
- Disease Prediction Result
- Admin Dashboard (if applicable)

---

## 🎯 Future Enhancements

- Support more plant species and diseases.
- Deploy the application on cloud platforms.
- Mobile application integration.
- Real-time disease detection using a smartphone camera.
- Multilingual support.
- Improved model accuracy using transfer learning.

---

## 👩‍💻 Author

**Akshitha Gannoju**

Final Year B.Tech (Information Technology)

---

## ⭐ If you found this project useful, consider giving it a star!
