from .authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated

class FirebaseAuthMixin():
    permission_classes = (IsAuthenticated,)
    authentication_classes = (FirebaseAuthentication,)
