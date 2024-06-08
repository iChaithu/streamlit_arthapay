import streamlit as st 
from streamlit_option_menu import option_menu
from apicaller import make_api_request, register_user

st.set_page_config(page_title="ArthaPay", page_icon=":memo:", layout="wide") 

def home():
    st.write("You are in home")
    return

if st.query_params:home()
else:
    option = st.sidebar.selectbox("Choose The Mode:", ["Login", "Sign Up"])
    if option == "Login":
        st.title("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            response = make_api_request("http://127.0.0.1:8080/login", username, password)
            st.write(response)
            st.write(response['access_token'])
                
            if response['access_token']:
                st.query_params["token"] = response['access_token']
                st.success("Logged in successfully!")
                st.markdown(f"<meta http-equiv='refresh' content='1;URL=/?user_id={response['access_token']}'>", unsafe_allow_html=True)
            else:
                st.write("re try..")
    elif option == "Sign Up": 
        st.header("Sign Up Form")
        payload = {
        "first_name": st.text_input("First Name"),
        "last_name": st.text_input("Last Name"),
        "password": st.text_input("Password", type="password"),
        "email": st.text_input("Email"),
        "phone": st.text_input("Phone"),
        "date_of_birth": st.date_input("Date of Birth"),
        "address": st.text_area("Address"),
        "wallet": "0",  # Default wallet value
        "user_type": "user",  # Default user type
        "kyc_status": "pending" }

        if st.button("Submit"):
            response = register_user("http://127.0.0.1:8080/register",payload)            
            st.write(response)