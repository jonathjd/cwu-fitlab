import streamlit as st
from google.cloud import firestore
from database import get_admin_password, enter_client_vars
import datetime

st.set_page_config(
    page_title="CWU Admin",
    layout='wide'
)

with st.sidebar:
    st.markdown(
        '<img src="https://github.com/jonathjd/cwu-fitlab/blob/main/img/cwu-long.png?raw=true" alt="0" style="width: 304px;margin-top: -400px;">',
        unsafe_allow_html=True
    )

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == get_admin_password():
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.title("Welcome Technician!")
    with st.expander("Input client data"):
        with st.form("Data"):
            d = str(datetime.date.today())
            client_identifier = st.text_input("Client ID (initials + birthday e.g. JD01171996)")
            age = st.text_input("Age")
            height = st.text_input("Height (in)")
            weight = st.text_input("Weight (lbs)")
            rest_hr = st.text_input("Resting heart rate")
            sys = st.text_input("Systolic blood pressure")
            dias = st.text_input("Diastolic blood pressure")
            caliper = st.text_input("Estimated body fat % (skin fold)")
            tank = st.text_input("Estimated body fat % (hydrostatic)")
            vo2 = st.text_input("Estimated VO2max")
            st.warning("Please make sure these values are correct before submitting", icon="⚠️")
            sub = st.form_submit_button("Submit")

    if sub:
        enter_client_vars(d, client_identifier, age, height, weight, rest_hr, sys, dias, caliper, tank, vo2)
        st.balloons()
        st.success("Thanks for the data!")
