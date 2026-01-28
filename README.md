# Fair Promotion Prediction AI

**A machine learning solution to eliminate algorithmic bias in HR decisions.**

##  Project Overview
This project analyzes staff promotion data for a multi-sector trading firm. Historical data revealed that the company's manual promotion process was statistically biased towards:
* **Specific Regions:** Staff from certain states were promoted at 2x the rate of others.
* **Recruitment Channels:** "Special Referral" candidates had a significant advantage over standard applicants.

To solve this, I engineered a **"Blind Justice"** machine learning model. This system explicitly removes demographic and connection-based features, forcing the algorithm to assess candidates purely on meritocratic data (KPIs, Training Scores, and Performance History).

##  Key Features
* **Bias Audit:** Statistical analysis identifying skew in historical promotion rates.
* **Blind Protocol:** Feature engineering strategy that safeguards against demographic bias.
* **Optimized Model:** `HistGradientBoostingClassifier` tuned via `RandomizedSearchCV` for maximum F1-Score.
* **Interactive App:** A Streamlit dashboard for HR managers to test candidate eligibility in real-time.

##  Tech Stack
* **Python** (Data Analysis & Modeling)
* **Scikit-Learn** (Machine Learning)
* **Streamlit** (Web Deployment)
* **Pandas/NumPy** (Data Manipulation)
* **Matplotlib** (Data Visualization)

##  Project Structure

- **`app.py`**: The main Streamlit application script.
- **`data/`**: Contains the raw datasets (`promotion_dataset(1).csv`) and the project case study.
- **`models/`**: Stores the serialized machine learning model (`promotion_model.pkl`) and the data encoder.
- **`notebooks/`**: Jupyter notebooks and HTML reports used for exploratory data analysis (EDA) and model training.
- **`requirements.txt`**: List of Python libraries required to run the project.

##  Model Performance
The Blind Justice model acts as an objective Second Opinion for HR.
* **Precision:** High reliability in identifying true top performers.
* **Recall:** Optimized to ensure deserving candidates are not overlooked.
* **Fairness:** Zero weight given to State of Origin, Gender, or Recruitment Channel.