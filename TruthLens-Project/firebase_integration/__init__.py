import os
import firebase_admin
from firebase_admin import credentials

# Configure the path to your Firebase Service Account Key JSON file
service_account_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'config',
    'firebase_service_account.json'
)

# Initialize the Firebase Admin SDK with the service account key
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)
