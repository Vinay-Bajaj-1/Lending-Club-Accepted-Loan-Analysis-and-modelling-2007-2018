import streamlit as st
import datetime

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

    # Display the collected input
    if st.button("Submit"):
        st.success("Loan Application Submitted!")
        st.write("Loan Amount:", loan_amnt)
        st.write("Term:", term)
        st.write("Interest Rate:", int_rate)
        st.write("Installment:", installment)
        st.write("Sub Grade:", sub_grade)
        st.write("Home Ownership:", home_ownership)
        st.write("Annual Income:", annual_inc)
        st.write("Verification Status:", verification_status)
        st.write("Purpose:", purpose)
        st.write("Debt-to-Income Ratio:", dti)
        st.write("Earliest Credit Line:", earliest_cr_line)
        st.write("Open Accounts:", open_acc)
        st.write("Public Records:", pub_rec)
        st.write("Revolving Balance:", revol_bal)
        st.write("Revolving Utilization:", revol_util)
        st.write("Total Accounts:", total_acc)
        st.write("Initial List Status:", initial_list_status)
        st.write("Application Type:", application_type)
        st.write("Mortgage Accounts:", mort_acc)
        st.write("Public Record Bankruptcies:", pub_rec_bankruptcies)

if __name__ == "__main__":
    main()
