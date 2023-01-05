from google.cloud import firestore

# Connect to database
db = firestore.Client.from_service_account_json("firestore-key.json")

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
        doc_ref = db.collection("clients").document(date)
        doc_ref.set({
            "clientid": client_id,
            "age": age,
            "height": height,
            "weight": weight,
            "rest_hr": rest_hr,
            "sys": sys,
            "dias": dias,
            "skinfold": caliper,
            "hydrostatic": tank,
            "vo2": vo2
        })


# create a ref to the example login
# example_login = db.collection("admin").document("login")

# example = example_login.get()

# doc_ref = db.collection("admin").document("Example_Person")
# doc_ref.set({
#     "username": "Joe",
#     "password": "JoeShmoe"
# })

# admin_ref = db.collection("admin")
