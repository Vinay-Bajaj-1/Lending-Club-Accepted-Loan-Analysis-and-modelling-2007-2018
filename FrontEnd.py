import streamlit as st
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

def preprocess_data(user_data):
    columns = ['loan_amnt', 'term', 'int_rate', 'installment', 'annual_inc',
           'dti', 'earliest_cr_line', 'open_acc', 'pub_rec',
           'revol_bal', 'revol_util', 'total_acc', 'mort_acc',
           'pub_rec_bankruptcies', 'sub_grade_A2', 'sub_grade_A3', 'sub_grade_A4',
           'sub_grade_A5', 'sub_grade_B1', 'sub_grade_B2', 'sub_grade_B3',
           'sub_grade_B4', 'sub_grade_B5', 'sub_grade_C1', 'sub_grade_C2',
           'sub_grade_C3', 'sub_grade_C4', 'sub_grade_C5', 'sub_grade_D1',
           'sub_grade_D2', 'sub_grade_D3', 'sub_grade_D4', 'sub_grade_D5',
           'sub_grade_E1', 'sub_grade_E2', 'sub_grade_E3', 'sub_grade_E4',
           'sub_grade_E5', 'sub_grade_F1', 'sub_grade_F2', 'sub_grade_F3',
           'sub_grade_F4', 'sub_grade_F5', 'sub_grade_G1', 'sub_grade_G2',
           'sub_grade_G3', 'sub_grade_G4', 'sub_grade_G5',
           'home_ownership_MORTGAGE', 'home_ownership_NONE',
           'home_ownership_OTHER', 'home_ownership_OWN', 'home_ownership_RENT',
           'verification_status_Source Verified', 'verification_status_Verified',
           'purpose_credit_card', 'purpose_debt_consolidation',
           'purpose_educational', 'purpose_home_improvement', 'purpose_house',
           'purpose_major_purchase', 'purpose_medical', 'purpose_moving',
           'purpose_other', 'purpose_renewable_energy', 'purpose_small_business',
           'purpose_vacation', 'purpose_wedding', 'initial_list_status_w',
           'application_type_Joint App']

    df = pd.DataFrame(columns = columns)
    df.loc[0] = False


    # 0 - 14
    df.iloc[0, :14] = user_data.iloc[0, :14]

    #handling categorical variables
    # 14 - 47
    for i in df.iloc[:, 14:47].columns:
        if i.split('_')[-1] == user_data['sub_grade'][0]:
            df[i] = True

    #47 - 52
    for i in df.iloc[:, 48:53].columns:
        if i.split('_')[-1] == user_data['home_ownership'][0]:
            df[i] = True

    #53 - 54
    for i in df.iloc[:, 53:55].columns:
        if i.split('_')[-1] == user_data['verification_status'][0]:
            df[i] = True

    #55 - 67
    for i in df.iloc[:, 55:68].columns:
        temp = user_data['purpose'].str.replace(' ', '_').str.lower()
        temp2 = i.split('purpose_')
        if temp[0] ==  temp2[-1]:
            df[i] = True
    # 68        
    if user_data['application_type'][0] == 'Joint App':
        df['application_type_Joint App'] = True

    if user_data['initial_list_status'][0] == 'w':
        df['initial_list_status_w'] = True


    #scaling
    loaded_scaler = joblib.load('min_max_scaler.pkl')
    scaled_data = loaded_scaler.transform(df)

    return scaled_data    

def main():
    st.title("Loan Application Form")

    # Get user input for various fields
    loan_amnt = st.number_input("Loan Amount ($)", min_value=0, step=1)
    term = st.selectbox("Term", ["36 months", "60 months"])
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, step=0.01)
    installment = st.number_input("Installment ($)", min_value=0, step=1)
    sub_grade = st.selectbox("Sub Grade", ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5",
                                           "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5",
                                           "E1", "E2", "E3", "E4", "E5", "F1", "F2", "F3", "F4", "F5",
                                           "G1", "G2", "G3", "G4", "G5"])
    home_ownership = st.selectbox("Home Ownership", ["MORTAGE", "RENT", "OWN", "OTHER"])
    annual_inc = st.number_input("Annual Income ($)", min_value=0, step=1)
    verification_status = st.selectbox("Verification Status", ["Source Verified", "Verified"])
    purpose = st.selectbox("Purpose", ["Credit Card", "Debt Consolidation", "Home Improvement", "House",
                                       "Major Purchase", "Educational", "Medical", "Moving", "Renewable Energy",
                                       "Small Business", "Wedding", "Vacation", "Other"])
    dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01)
    earliest_cr_line = st.number_input("Earliest Credit Line Year", min_value=0, step=1)
    open_acc = st.number_input("Open Accounts", min_value=0, step=1)
    pub_rec = st.number_input("Public Records", min_value=0, step=1)
    revol_bal = st.number_input("Revolving Balance ($)", min_value=0, step=1)
    revol_util = st.number_input("Revolving Utilization Rate (%)", min_value=0.0, max_value=100.0, step=0.01)
    total_acc = st.number_input("Total Accounts", min_value=0, step=1)
    initial_list_status = st.selectbox("Initial List Status", ["W", "T"])
    application_type = st.selectbox("Application Type", ["Joint", "Individual"])
    mort_acc = st.number_input("Mortgage Accounts", min_value=0, step=1)
    pub_rec_bankruptcies = st.number_input("Public Record Bankruptcies", min_value=0, step=1)

    
    user_data = pd.DataFrame({
        'loan_amnt': [loan_amnt],
        'term': [term.split()[0]],
        'int_rate': [int_rate],
        'installment': [installment],
        'annual_inc': [annual_inc],
        'dti': [dti],
        'earliest_cr_line': [earliest_cr_line],
        'open_acc': [open_acc],
        'pub_rec': [pub_rec],
        'revol_bal': [revol_bal],
        'revol_util': [revol_util],
        'total_acc': [total_acc],
        'mort_acc': [mort_acc],
        'pub_rec_bankruptcies': [pub_rec_bankruptcies],
        
        'sub_grade': [sub_grade],
        'home_ownership': [home_ownership],
        'verification_status': [verification_status],
        'purpose': [purpose],
        'initial_list_status': [initial_list_status],
        'application_type': [application_type],
        
    })
    
    if st.button("Submit"):
        # Call the preprocessing function
        processed_data = preprocess_data(user_data)
        model_ann = load_model('ANN_model.h5')
        # Display the processed data
        st.subheader("Processed Application Data:")
        st.write(processed_data.shape)
        st.write(processed_data)
        #res= model_ann.predict(processed_data)
        #st.write(res)
        
        
if __name__ == "__main__":
    main()

