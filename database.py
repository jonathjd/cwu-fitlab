from google.cloud import firestore
import json
import streamlit as st
from google.oauth2 import service_account


# Connect to database
# db = firestore.Client.from_service_account_json("firestore-key.json")

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="cwu-fitlab")

def get_admin_username():
    doc_ref = db.collection("admin").document("Fitlab")
    doc = doc_ref.get()
    username = doc.to_dict()["username"]
    return username

def get_admin_password():
    doc_ref = db.collection("admin").document("Fitlab")
    doc = doc_ref.get()
    password = doc.to_dict()["password"]
    return password

def enter_client_vars(date, client_id, age, height, weight, rest_hr, sys, dias, caliper, gold_skinfold, vo2, assessment, vo2_assess, sit_reach, alt_method, push_up):
        doc_ref = db.collection("clients").document(client_id).collection("data").document(date)
        doc_ref.set({
            "age": age,
            "height": height,
            "weight": weight,
            "rest_hr": rest_hr,
            "sys": sys,
            "dias": dias,
            "skinfold": caliper,
            "gold_skinfold": gold_skinfold,
            "alt_method": alt_method,
            "vo2": vo2,
            "sit_reach": sit_reach,
            "assessment": assessment,
            "vo2_assess": vo2_assess,
            "push_up": push_up
        }, merge=True)

def client_bool(client_id):
    if client_id == "":
        return False

    doc_ref = db.collection("clients").document(client_id).collection("data")
    val_ref = doc_ref.get()
    if val_ref == []:
        return False
    return True

def fetch_client_data(client_id):
    if client_id == "":
        return 

    doc_ref = db.collection("clients").document(client_id).collection("data")
    val_ref = doc_ref.get()

    if val_ref == []:
        st.error("Client not found")
        return 

    dates = []
    for doc in val_ref:
        dates.append(doc.id)
    day = st.selectbox(
        label="Appointment Date",
        options=dates
    )
    client_dict = doc_ref.document(day).get().to_dict()
    return client_dict