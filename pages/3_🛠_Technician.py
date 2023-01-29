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
        with st.form("Data", clear_on_submit=True):
            client_identifier = st.text_input(label="Client ID (initials + birthday MMDDYYYY)", placeholder="e.g. EX01171996")
            d = st.date_input(
                label="Visit Date :date:",
                value=datetime.date.today()
                )
            d = str(d)
            sex = st.radio(
                label='Enter client sex',
                options=('M', 'F'),
                horizontal=True
            )
            assessment = st.radio(
                label="Select assessment type", 
                options=('Full fitness assessment', "Body composition only"),
                horizontal=True
            )
            age = st.text_input("Age")
            height = st.text_input("Height (in)")
            weight = st.text_input("Weight (lbs)")
            rest_hr = st.text_input("Resting heart rate (bpm)")
            sys = st.text_input("Systolic blood pressure (mmHg)")
            dias = st.text_input("Diastolic blood pressure (mmHg)")
            caliper = st.text_input("Estimated body fat % (skin fold)")
            alt_method = st.radio(
                label="Bod pod or hydrostatic weighing?", 
                options=('Bod pod', "Hydrostatic"),
                horizontal=True
            )
            gold_skinfold = st.text_input("Estimated body fat % (bod pod/hydrostatic)")
            st.info("**Leave the rest of the form blank if body composition only**")
            vo2 = st.text_input("Estimated VO2max (ml/kg/min)")
            vo2_assess = st.radio(
                label="YMCA or Queens College?", 
                options=('YMCA', "Queens College Step Test"),
                horizontal=True
            )
            sit_reach = st.text_input("Sit and Reach (cm)")
            push_up = st.text_input("Push ups")
            push_up_form = st.radio(
                label="Were the push ups performed on the knees?",
                options=('Yes', 'No'),
                horizontal=True
            )
            st.warning("Please make sure these values are correct before submitting", icon="⚠️")
            sub = st.form_submit_button("Submit")

    if sub:
        enter_client_vars(d, client_identifier, age, height, weight, rest_hr, sys, dias, caliper, gold_skinfold, vo2, assessment, vo2_assess, sit_reach, alt_method, push_up, sex, push_up_form)
        st.balloons()
        st.success("Thanks for the data!")
