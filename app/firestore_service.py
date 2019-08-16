"""firestore module"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

PEOJECT_ID = 'alquilat-143920'
CREDENTIAL = credentials.ApplicationDefault()
APP = firebase_admin.initialize_app(CREDENTIAL, {
    'projectId': PEOJECT_ID,
    })
DB = firestore.client()


def get_users():
    """Return all users"""
    return DB.collection('users').get()


def get_user(user_id):
    """return one user"""
    return DB.collection('users').document(user_id).get()


def get_todos(user_id):
    """return all todos"""
    return DB.collection('users')\
    .document(user_id)\
    .collection('todos').get()
