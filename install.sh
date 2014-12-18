#!/bin/sh
#purpose: setup geodjango example from POSTGIS cookbook
cd ~/virtualenvs/
virtualenv --no-site-packages chp09-env
source chp09-env/bin/activate
pip install pillow django psycopg2

DJANGOPATH="/srv/ows.bfh.ch/geodjango"
#mkdir -p DJANGOPATH
#cd DJANGOPATH
#django-admin.py startproject rehprojekt
#django-admin.py startapp sightings

