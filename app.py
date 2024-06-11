import streamlit as st
from streamlit_option_menu import option_menu

def home():
    st.sidebar.title("ArthaPay")
    with st.sidebar:
        selected_page = option_menu("Arthapay", ["Pay Out", "Pay IN",  "History", 'LogOut'])

    if selected_page == "Pay Out":

        option = option_menu(None, [ "Q Transfer", "Money Transfer", 'AEPS',"PayOut"],
                                    menu_icon="cast", default_index=0, orientation="horizontal",
                                    icons=['house', 'bi bi-pass-fill', "bi bi-gear", 'bi bi-peace'],)
        
        if option == "Q Transfer":
            cols, cols1, cols3 = st.columns([1,2,1])
            with cols1:
                st.write("#")
                with st.form(key='q_transfer_form'):
                    customer_mobile, bank, account_number = st.text_input('Customer Mobile'), st.text_input('Bank'), st.text_input('Account Number')
                    ifsc, name, amount = st.text_input('IFSC'), st.text_input('Name'), st.number_input('Amount', min_value=0.0, format="%.2f")
                    submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    st.write("Details submitted:")
                    st.write(f"Customer Mobile: {customer_mobile}")
                    st.success("Transaction will be processed after the API Integration..")
        
        elif option == "Money Transfer":
            cols, cols1, cols3 = st.columns([1,2,1])
            with cols1:
                st.write("#")
                with st.form(key='Money_transfer_form'):
                    m = st.text_input('Customer Mobile')
                    submit_button = st.form_submit_button(label='Submit')
                if submit_button and m:
                    st.success("Service available till here only...")

        elif option == "AEPS":
            cols, cols1, cols3 = st.columns([1,2,1])
            with cols1:
                st.write("#")
                with st.form(key='AEPS_form'):
                    m = st.text_input('Enter AADAAR Number..')
                    submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    st.success("Service available till here only...")

        elif option == "PayOut":
            cols, cols1, cols3 = st.columns([1,1,1])
            with cols:
                st.subheader("Self PayOut")
                st.write("###")
                st.info("already saved accounts will be displayed here...")
                st.info("Waiting for API integration")
            with cols1:
                st.subheader("Quick Self PayOut")
                st.write("###")
                st.info("Quick payout to user desired accounts with out adding them")
                with st.form(key='QSPayout_form'):
                    bank, account_number =  st.text_input('Bank'), st.text_input('Account Number')
                    ifsc, name, amount = st.text_input('IFSC'), st.text_input('Name'), st.number_input('Amount', min_value=0.0, format="%.2f")
                    submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    st.success("Service available till here only...")   
            with cols3:
                st.subheader("Add/Delete Account for self Payout")
                st.write("###")
                st.info("Shows saved accounts and gives options to delete or add new ")
                st.info("Waiting for API integration")


    
    elif selected_page == "Pay IN":st.info("Waiting for API integration")
    elif selected_page == "History":st.info("Waiting for API integration")
    elif selected_page == "LogOut":st.query_params.clear();st.markdown(f"<meta http-equiv='refresh' content='1;URL=/'>", unsafe_allow_html=True)

