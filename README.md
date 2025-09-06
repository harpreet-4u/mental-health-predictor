# 🧠 Student Mental Health Prediction Project

This project predicts a student's **mental stress level during exams** using their lifestyle and academic habits. It takes simple inputs like sleep hours, study time, social media usage, diet, and gives an instant stress-level prediction.

---

## 🚀 Live Project

🔗 [Click here to try the Mental Health Prediction App](https://studentmentalhealthprediction.streamlit.app/)  

---

## 📊 Features Used for Prediction

- Gender  
- Age  
- Hours of Sleep  
- Study Time  
- Social Media Usage  
- Exercise  
- Balanced Diet  
- Family Support  
- Academic Pressure  

---

## 🧠 How it Works

1. A synthetic dataset of 1000 students was created with lifestyle and academic patterns.
2. A **Decision Tree Classifier** model was trained on this dataset.
3. The trained model is saved and used in a **Streamlit app** to predict mental stress levels.
4. Users fill in a short form, and the model gives a result like "Low", "Moderate", or "High" stress.

---

## 💻 How to Run Locally

### Step 1: Clone this repository

```bash
git clone https://github.com/harpreet-4u/student-mental-health-prediction.git
cd student-mental-health-prediction
```

### Step 2: Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
student-mental-health-prediction/
│
├── app.py                           # Streamlit web app
├── Mental_Health_Prediction_Notebook.ipynb   # ML training and analysis
├── mental_health_model.pkl         # Trained ML model file
├── label_encoder.pkl               # Encoded label classes
├── mental_health_dataset_1000.csv  # Dataset (1000 student records)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .ipynb_checkpoints/             # Jupyter auto-saved versions
```

---

## 📌 Disclaimer

This is an educational project and should not be used for actual mental health diagnosis. If someone is struggling, please encourage them to talk to a professional.

---

## 👨‍💻 Created By

**Harpreet Singh**  
B.Tech CSE Student  
DCRUST University  
