#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

def preprocess_data(df):
    dummies = ['Sub Grade', 'Home Ownership', 'Verification Status', 'Purpose', 'Initial List Status', 'Application Type']
    main_df = pd.get_dummies(df, columns = dummies, drop_first = True)
    return main_df
    

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
    home_ownership = st.selectbox("Home Ownership", ["Mortgage", "Rent", "Own", "Other"])
    annual_inc = st.number_input("Annual Income ($)", min_value=0, step=1)
    verification_status = st.selectbox("Verification Status", ["Source Verified", "Verified"])
    purpose = st.selectbox("Purpose", ["Credit Card", "Debt Consolidation", "Home Improvement", "House",
                                       "Major Purchase", "Educational", "Medical", "Moving", "Renewable Energy",
                                       "Other", "Small Business", "Wedding", "Vacation"])
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

    # Display the collected information
    user_data = pd.DataFrame({
        'Loan Amount': [loan_amnt],
        'Term': [term],
        'Interest Rate': [int_rate],
        'Installment': [installment],
        'Sub Grade': [sub_grade],
        'Home Ownership': [home_ownership],
        'Annual Income': [annual_inc],
        'Verification Status': [verification_status],
        'Purpose': [purpose],
        'Debt-to-Income Ratio': [dti],
        'Earliest Credit Line Year': [earliest_cr_line],
        'Open Accounts': [open_acc],
        'Public Records': [pub_rec],
        'Revolving Balance': [revol_bal],
        'Revolving Utilization Rate': [revol_util],
        'Total Accounts': [total_acc],
        'Initial List Status': [initial_list_status],
        'Application Type': [application_type],
        'Mortgage Accounts': [mort_acc],
        'Public Record Bankruptcies': [pub_rec_bankruptcies]
    })
    
    if st.button("Submit"):
        # Call the preprocessing function
        processed_data = preprocess_data(user_data)

        # Display the processed data
        st.subheader("Processed Application Data:", processed_data.shape)
        st.write(processed_data)
        
        
if __name__ == "__main__":
    main()


# In[ ]:




