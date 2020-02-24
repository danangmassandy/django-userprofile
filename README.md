# django-userprofile

1. Set Google Map API Key in .env file using key=GOOGLE_MAPS_API_KEY
2. Install dependencies
    pip install -r requirements.txt
3. Run initial migration scripts
    python manage.py migrate
4. Setup admin superuser
    python manage.py createsuperuser
5. Create users and profiles from admin site
    http://127.0.0.1:8000/admin/
6. MapView page:
    http://127.0.0.1:8000/
