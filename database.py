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

def enter_client_vars(date, client_id, age, height, weight, rest_hr, sys, dias, caliper, tank, vo2):
        doc_ref = db.collection("clients").document(date).collection("data").document(client_id)
        doc_ref.set({
            "age": age,
            "height": height,
            "weight": weight,
            "rest_hr": rest_hr,
            "sys": sys,
            "dias": dias,
            "skinfold": caliper,
            "hydrostatic": tank,
            "vo2": vo2
        }, merge=True)
