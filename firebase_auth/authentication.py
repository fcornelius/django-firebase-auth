from rest_framework import authentication
from django.contrib.auth.models import User
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os
from django.conf import settings

json = os.path.join(settings.KEYFILES_DIR, settings.FIREBASE_KEY)
cred = credentials.Certificate(json)
default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            pass

        if not id_token or not decoded_token:
            return None

        uid = decoded_token.get('uid')
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('The user does not exist')

        return (user, None)
