from django.apps import AppConfig

class ThebandConfig(AppConfig):
    """
    Configuration for the 'theband' application.

    This class is used to configure the 'theband' Django app,
    specifying the name and the default auto field type for models.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theband'
