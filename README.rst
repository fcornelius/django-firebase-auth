=====
django-firebase-auth
=====

django-firebase-auth is a authentication provider for Google's `Firebase Authentication Service <https://firebase.google.com/products/auth/>`_ which blends right into django-rest-framework.
Simply setup your Firebase keyfile location and mark views which need authentication with the FirebaseAuthMixin authentication class.


Detailed documentation is in the "docs" directory.

Installation
-----------

Install via pip::

    pip install django-firebase-auth

(This will also install dependencies `django-rest-framework <https://github.com/encode/django-rest-framework/>`_ and `firebase-admin <https://github.com/firebase/firebase-admin-python/>`_.)

Quick start
-----------

1. Add "firebase_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'firebase_auth',
    ]

2. Specify a location for your Firebase keyfile with the settings::

    KEYFILES_DIR = os.path.join(BASE_DIR, 'keyfiles')
    FIREBASE_KEY = '<your-key-file>.json'
    
   And place the json key inside BASE_DIR/keyfiles.

3. Either set FirebaseAuthentication as the global default authentication class in settings, like::
    
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': ('firebase_auth.authentication.FirebaseAuthentication', ),
    }

   Or extend specific views from FirebaseAuthMixin, like::

    from firebase_auth import FirebaseAuthMixin
    class MyModelViewSet(FirebaseAuthMixin, viewsets.ModelViewSet)
        ...
    
   Note that the auth mixin has to be the first class extended by the view.

4. Create your users with the Firebase user ID as user ID.
   Inside your views, you can access the user reference like you're used to with  request.user
   

