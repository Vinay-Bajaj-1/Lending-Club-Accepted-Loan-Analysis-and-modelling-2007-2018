import streamlit as st
import datetime
import pandas as pd

def main():
    st.title("Loan Application Form")

    # Input fields for various features
    loan_amnt = st.number_input("Loan Amount", min_value=1, step=1)
    term = st.selectbox("Term", ["36 months", "60 months"])
    int_rate = st.number_input("Interest Rate", min_value=0.0, step=0.01)
    installment = st.number_input("Installment", min_value=1, step=1)
    sub_grade = st.selectbox("Sub Grade", ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5",
                                           "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5",
                                           "E1", "E2", "E3", "E4", "E5", "F1", "F2", "F3", "F4", "F5",
                                           "G1", "G2", "G3", "G4", "G5"])
    home_ownership = st.selectbox("Home Ownership", ["Mortgage", "Rent", "Own", "Other"])
    annual_inc = st.number_input("Annual Income", min_value=0, step=1)
    verification_status = st.selectbox("Verification Status", ["Source Verified", "Verified"])
    purpose = st.selectbox("Purpose", ["Credit Card", "Debt Consolidation", "Home Improvement", "House",
                                       "Major Purchase", "Educational", "Medical", "Moving", "Renewable Energy",
                                       "Other", "Small Business", "Wedding", "Vacation"])
    dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01)
    earliest_cr_line = st.date_input("Earliest Credit Line")
    open_acc = st.number_input("Open Accounts", min_value=0, step=1)
    pub_rec = st.number_input("Public Records", min_value=0, step=1)
    revol_bal = st.number_input("Revolving Balance", min_value=0, step=1)
    revol_util = st.number_input("Revolving Utilization", min_value=0.0, step=0.01, max_value=100.0)
    total_acc = st.number_input("Total Accounts", min_value=0, step=1)
    initial_list_status = st.selectbox("Initial List Status", ["w", "t"])
    application_type = st.selectbox("Application Type", ["Joint", "Individual"])
    mort_acc = st.number_input("Mortgage Accounts", min_value=0, step=1)
    pub_rec_bankruptcies = st.number_input("Public Record Bankruptcies", min_value=0, step=1)
    
    user_data = pd.DataFrame({
        'loan_amnt': [loan_amnt],
        'term': [term],
        'int_rate': [int_rate],
        'installment': [installment],
        'sub_grade': [sub_grade],
        'home_ownership': [home_ownership],
        'annual_inc': [annual_inc],
        'verification_status': [verification_status],
        'purpose': [purpose],
        'dti': [dti],
        'earliest_cr_line': [earliest_cr_line],
        'open_acc': [open_acc],
        'pub_rec': [pub_rec],
        'revol_bal': [revol_bal],
        'revol_util': [revol_util],
        'total_acc': [total_acc],
        'initial_list_status': [initial_list_status],
        'application_type': [application_type],
        'mort_acc': [mort_acc],
        'pub_rec_bankruptcies': [pub_rec_bankruptcies]
    })
    

    # Display the collected input
    if st.button("Submit"):
        st.success("Loan Application Submitted!")
        st.dataframe(user_data)

        # Preprocess the data
        preprocessed_data = preprocess_data(user_data)
        st.write("Preprocessed Data:")
        st.dataframe(preprocessed_data)
        

if __name__ == "__main__":
    main()
