from firebase_admin import credentials, initialize_app
from decouple import config


CREDENTIALS = config("GOOGLE_APPLICATION_CREDENTIALS")
COLLECTION_NAME = config("COLLECTION_NAME")
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")


cred = credentials.Certificate(CREDENTIALS)
app = initialize_app(cred)