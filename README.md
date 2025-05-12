# Software Developer Salary Prediction App

This project is a web-based application built using **Streamlit** that allows users to:
- **Predict software developer salaries** based on their country, education level, and experience.
- **Explore data** from the Stack Overflow Developer Survey 2020 using interactive visualizations.

---

## 📊 Features

- **Prediction Page**:
  - Input your country, education level, and years of experience.
  - Get an estimated salary based on a trained machine learning model.
  - Animated bar graph to visualize the predicted salary.

- **Explore Page**:
  - Visualizations of survey data by country, experience, and education level.
  - Interactive pie chart, scatter plot, and box plot using Plotly.

---

## 🚀 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/salary-prediction-app.git
cd salary-prediction-app
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Launch the app:
```bash
streamlit run app.py
```

---

## 📁 Files

- `app.py` - Main Streamlit app file.
- `predict_page.py` - Handles the salary prediction UI and logic.
- `explore_page.py` - Handles data exploration and visualization.
- `saved_steps.pkl` - Trained model and encoders.
- `survey_results_public.csv.gz` - Dataset from Stack Overflow (2020).
- `salary_prediction2.ipynb` - Notebook used for preprocessing and training.

---

## 📦 Dependencies

See `requirements.txt`

---

## 📚 Data Source

See `survey_results__public.csv.gz`

---
