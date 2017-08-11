import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os
from django.conf import settings

json = os.path.join(settings.KEYFILES_DIR, settings.FIREBASE_KEY)
cred = credentials.Certificate(json)
default_app = firebase_admin.initialize_app(cred)

