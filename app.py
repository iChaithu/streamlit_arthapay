import streamlit as st
from streamlit_option_menu import option_menu

def home():
    st.sidebar.title("ArthaPay")
    option = st.sidebar.radio("Choose The Mode:", ["Pay Out", "Pay IN", "History", "LogOut"])

    if option == "Pay Out":
        selected_page = option_menu(None, ["Dashboard", "Q Transfer",  "Money Transfer", 'AEPS'], 
        icons=['house', 'bi bi-pass-fill', "bi bi-gear", 'bi bi-peace'], 
        menu_icon="cast", default_index=3, orientation="horizontal",
        styles={"icon": {"color": "orange", "font-size": "25px"}, 
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"}})
    
    elif option == "Pay IN":st.write("Upcoming feature")
    elif option == "Pay IN":st.write("History")
    elif option == "Pay IN":st.write("LogOut")

