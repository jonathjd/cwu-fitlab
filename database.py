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
        doc_ref = db.collection("clients").document(client_id).collection("data").document(date)
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

def fetch_example_data(client_id):
    doc_ref = db.collection("clients").document(client_id).collection("data")
    dates = []
    val_ref = doc_ref.stream()
    for doc in val_ref:
        dates.append(doc.id)
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict())

    day = st.selectbox(
        label="Appointment Date",
        options=dates
    )
    client_ref = doc_ref.document(day).get().to_dict()
    st.write(client_ref['age'])

# create a ref to the example login
# example_login = db.collection("admin").document("login")

# example = example_login.get()

# st.write(f"The document is: ", example.id)
# st.write(f"The contents are: {example.to_dict()}")



# admin_ref = db.collection("admin")

# for doc in admin_ref.stream():
#     st.write("The id is: ", doc.id)
#     st.write("The contents are: ", doc.to_dict())