import firebase_admin
from firebase_admin import firestore

def create_user_document(uid):
    db = firestore.client()
    user_doc_ref = db.collection('users').document(uid)
    user_doc_ref.set({
        'factchecked_statement': '',
        'link_to_media': '',
        'source_links': [],
        'final_assessment': '',
        # Add more fields as necessary
    })
