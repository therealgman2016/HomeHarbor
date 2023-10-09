from django.apps import AppConfig


    
class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    def ready(self):
       # make_superuser = "python3 manage.py createsuperuser"
       print("-------------active-------------")

