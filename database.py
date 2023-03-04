from google.cloud import firestore
import json
import streamlit as st
from google.oauth2 import service_account
import pandas as pd
import numpy as np
import csv


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


def enter_client_vars(date, client_id, age, height, weight, rest_hr, sys, dias, caliper, gold_skinfold, vo2, assessment, vo2_assess, sit_reach, alt_method, push_up, sex, push_up_form):
        doc_ref = db.collection("clients").document(client_id).collection("data").document(date)
        doc_ref.set({
            "age": age,
            'sex': sex,
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
            "push_up": push_up,
            "push_up_form": push_up_form,
        }, merge=True)
        return


def client_bool(client_id):
    if client_id == "":
        return False

    doc_ref = db.collection("clients").document(client_id).collection("data")
    val_ref = doc_ref.get()
    if val_ref == []:
        return False
    return True


def fetch_agg_df(client_id):
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
    
    # make pandas df
    df = pd.DataFrame()
    for day in dates:
        doc = doc_ref.document(day).get().to_dict()
        df = df.append(doc, ignore_index=True)

    # Clean dataframe
    # convert dates column to date object
    df['Date'] = dates
    df['Date'] = pd.to_datetime(df['Date'])

    # Subset cols & rename
    df_subset = df[['sys', 'gold_skinfold', 'age', 'push_up', 'sit_reach', 'rest_hr', 'height', 'vo2', 'dias', 'weight', 'vo2_assess', 'Date', 'sex']]
    renamed_df = df_subset.rename(columns={
        'weight': 'Weight (lbs)',
        'vo2_assess': 'VO2 Assessment', 
        'push_up': 'Push Ups', 
        'gold_skinfold': 'Body Fat (%)', 
        'height': 'Height (in)', 
        'sys': 'Systolic BP (mmHg)', 
        'dias': 'Diastolic BP (mmHg)', 
        'rest_hr': 'Resting Heart Rate (BPM)', 
        'sit_reach': 'Sit and Reach (cm)', 
        'age': 'Age', 
        'vo2': 'VO2Max (ml/kg/min)', 
        'Date': 'Visit Date',
        'sex': 'Sex'
        }).copy()

    # Change dtype of cols
    renamed_df[['Systolic BP (mmHg)', 'Push Ups', 'Resting Heart Rate (BPM)', 'Diastolic BP (mmHg)', 'Body Fat (%)', 'Sit and Reach (cm)', 'Height (in)', 'VO2Max (ml/kg/min)', 'Weight (lbs)']] = renamed_df[['Systolic BP (mmHg)', 'Push Ups', 'Resting Heart Rate (BPM)', 'Diastolic BP (mmHg)', 'Body Fat (%)', 'Sit and Reach (cm)', 'Height (in)', 'VO2Max (ml/kg/min)', 'Weight (lbs)']].apply(pd.to_numeric)
    return renamed_df


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
    
    # make pandas df
    df = pd.DataFrame()
    for day in dates:
        doc = doc_ref.document(day).get().to_dict()
        df = df.append(doc, ignore_index=True)

    # Clean dataframe
    # convert dates column to date object
    df['Date'] = dates
    df['Date'] = pd.to_datetime(df['Date'])

    # Subset cols & rename
    df_subset = df[['sys', 'gold_skinfold', 'age', 'push_up', 'sit_reach', 'rest_hr', 'height', 'vo2', 'dias', 'weight', 'vo2_assess', 'Date', 'sex']]
    renamed_df = df_subset.rename(columns={
        'weight': 'Weight (lbs)',
        'vo2_assess': 'VO2 Assessment', 
        'push_up': 'Push Ups', 
        'gold_skinfold': 'Body Fat (%)', 
        'height': 'Height (in)', 
        'sys': 'Systolic BP (mmHg)', 
        'dias': 'Diastolic BP (mmHg)', 
        'rest_hr': 'Resting Heart Rate (BPM)', 
        'sit_reach': 'Sit and Reach (cm)', 
        'age': 'Age', 
        'vo2': 'VO2Max (ml/kg/min)', 
        'Date': 'Visit Date',
        'sex': 'Sex'
        }).copy()

    # Change dtype of cols
    renamed_df[['Systolic BP (mmHg)', 'Push Ups', 'Resting Heart Rate (BPM)', 'Diastolic BP (mmHg)', 'Body Fat (%)', 'Sit and Reach (cm)', 'Height (in)', 'VO2Max (ml/kg/min)', 'Weight (lbs)']] = renamed_df[['Systolic BP (mmHg)', 'Push Ups', 'Resting Heart Rate (BPM)', 'Diastolic BP (mmHg)', 'Body Fat (%)', 'Sit and Reach (cm)', 'Height (in)', 'VO2Max (ml/kg/min)', 'Weight (lbs)']].apply(pd.to_numeric)
    return renamed_df

def fetch_agg_data():
    collection_ref = db.collection("clients")
    subcollections = collection_ref.list_documents()
    client_list = []
    # Create pandas df to export as csv
    df = pd.DataFrame()

    # fetch client ID's and append to dict
    for subcollection in subcollections:
        client_list.append(subcollection.id)

    for c in client_list:
        data = fetch_client_data(c)
        data["Client"] = c
        df = pd.concat([df, data], axis=0)

    df.index = range(0,len(df))

    return df    

