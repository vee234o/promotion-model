import streamlit as st
import pandas as pd
import joblib

# --- 1. SETUP & LOADING ---
st.set_page_config(page_title="Yakub Promotion AI", page_icon="⚖️")

@st.cache_resource
def load_data():
    try:
        model = joblib.load('promotion_model.pkl')
        encoder = joblib.load('promotion_encoder.pkl')
        return model, encoder
    except FileNotFoundError:
        return None, None

model, encoder = load_data()

# --- 2. HEADER ---
st.title("⚖️ Blind Justice Promotion Tool")
if model is None:
    st.error("Error: 'promotion_model.pkl' or 'promotion_encoder.pkl' not found.")
    st.stop()

st.markdown("""
This tool predicts promotion eligibility based purely on **Performance & Merit**. 
*State of Origin* and *Recruitment Channel* are removed to ensure fairness.
""")

# --- 3. INPUT FORM (Sidebar) ---
st.sidebar.header("Candidate Profile")

def get_user_input():
    # A. Categorical Inputs (Must match the options in your data)
    division = st.sidebar.selectbox('Division', [
        'Commercial Sales and Marketing', 'Customer Support and Field Operations',
        'Information and Strategy', 'Information Technology and Solution Support',
        'Sourcing and Purchasing', 'Business Finance Operations',
        'People/HR Management', 'Regulatory and Legal services', 'Research and Innovation'
    ])
    
    qualification = st.sidebar.selectbox('Qualification', [
        'First Degree or HND', 'MSc, MBA and PhD', 'Non-University Education'
    ])
    
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    marital_status = st.sidebar.selectbox('Marital Status', ['Married', 'Single', 'Not_Sure'])
    foreign_schooled = st.sidebar.radio("Foreign Schooled?", ['Yes', 'No'])
    past_disciplinary = st.sidebar.radio("Past Disciplinary Action?", ['Yes', 'No'])
    intra_movement = st.sidebar.radio("Prev. Intra-Dept Movement?", ['Yes', 'No'])
    prev_employers = st.sidebar.selectbox("No. of Previous Employers", ['0', '1', '2', '3', '4', '5', 'More than 5'])

    # B. Numerical Inputs
    training_attended = st.sidebar.number_input('Trainings Attended', 2, 11, 2)
    training_score = st.sidebar.slider('Average Training Score', 0, 100, 50)
    last_perf_score = st.sidebar.number_input('Last Performance Score', 0.0, 14.0, 7.5, step=0.5)
    age_year = st.sidebar.number_input('Year of Birth', 1950, 2005, 1990)
    recruit_year = st.sidebar.number_input('Year of Recruitment', 1980, 2024, 2015)
    
    # C. Logic Inputs (Targets/Awards) -> Convert Yes/No to 1/0
    targets_met = 1 if st.sidebar.radio("Targets Met?", ['Yes', 'No']) == 'Yes' else 0
    previous_award = 1 if st.sidebar.radio("Previous Award?", ['Yes', 'No']) == 'Yes' else 0

    # Store in DataFrame (Columns must match X_train exactly!)
    data = {
        'Division': division,
        'Qualification': qualification,
        'Gender': gender,
        'Trainings_Attended': training_attended,
        'Year_of_birth': age_year,
        'Last_performance_score': last_perf_score,
        'Year_of_recruitment': recruit_year,
        'Targets_met': targets_met,
        'Previous_Award': previous_award,
        'Training_score_average': training_score,
        'Foreign_schooled': foreign_schooled,
        'Marital_Status': marital_status,
        'Past_Disciplinary_Action': past_disciplinary,
        'Previous_IntraDepartmental_Movement': intra_movement,
        'No_of_previous_employers': prev_employers
    }
    return pd.DataFrame([data])

input_df = get_user_input()

# --- 4. PREDICTION LOGIC ---
st.subheader("Candidate Summary")
st.dataframe(input_df)

if st.button("Assess Eligibility"):
    # 1. Identify Categorical Columns (Same as training)
    cat_cols = [
        'Division', 'Qualification', 'Gender', 'Foreign_schooled', 
        'Marital_Status', 'Past_Disciplinary_Action', 
        'Previous_IntraDepartmental_Movement', 'No_of_previous_employers'
    ]
    
    # 2. Encode the Input (Text -> Numbers)
    try:
        input_df[cat_cols] = encoder.transform(input_df[cat_cols])
        
        # 3. Predict
        pred = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        # 4. Display Result
        st.markdown("---")
        if pred == 1:
            st.success(f"RECOMMENDED FOR PROMOTION (Confidence: {prob:.1%})")
        else:
            st.error(f"NOT RECOMMENDED** (Confidence: {prob:.1%})")
            
    except Exception as e:
        st.error(f"Error during prediction: {e}")