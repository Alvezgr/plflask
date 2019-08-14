import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'alquilat-143920'
credential = credentials.ApplicationDefault()
app = firebase_admin.initialize_app(credential, {
    'projectId': project_id,
    })
db = firestore.client()

def get_users():
    return db.collection('users').get()
