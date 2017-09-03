import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-firebase-auth',
    version='0.4',
    packages=find_packages(),
    install_requires=[
          'firebase-admin',
          'djangorestframework'
    ],
    include_package_data=True,
    license='BSD License', 
    description='A django-rest-framework authentication provider for Google\'s Firebase Authentication Service',
    long_description=README,
    author='Felix Cornelius',
    author_email='mail@felixcornelius.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
