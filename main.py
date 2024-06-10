import streamlit as st
from apicaller import *
from app import home

st.set_page_config(page_title="ArthaPay", page_icon=":memo:", layout="wide") 

if st.query_params.get("access_token"):
    home()
else: 
    st.sidebar.title("Authentication")
    option = st.sidebar.selectbox("Choose The Mode:", ["Login", "Sign Up"])

    if option == "Login":
        st.title("Login")

        if st.query_params.get("username"):
            st.write(f"Username: {st.query_params.get('username')}")
            password = st.text_input("Enter your password", type="password")
            if st.button("Login"):
                status, do = log_in("http://127.0.0.1:8080/login",st.query_params.get("username"), password )
                if status:  
                    if do['access_token']:
                        st.query_params["token"] = do['access_token']
                        st.success("Logged in successfully!")
                        st.markdown(f"<meta http-equiv='refresh' content='1;URL=/?access_token={do['access_token']}'>", unsafe_allow_html=True)
                else:
                    st.write(do)
        else:
            phone_number = st.text_input("Enter your phone number")
            if st.button("Submit"):
                status, username = get_username("http://127.0.0.1:8080/get_user", phone_number)
                if status:
                    st.write(username)
                    st.query_params["username"] = username['message']
                    st.success(f"Username found: {username}")
                    st.markdown(f"<meta http-equiv='refresh' content='1;URL=/?username={username['message']}'>", unsafe_allow_html=True)
                else:
                    st.error("Phone number not found")
