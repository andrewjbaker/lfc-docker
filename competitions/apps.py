from django.apps import AppConfig

class CompetitionsConfig(AppConfig):
    """A class that configures the Competitions db model in Django

    :param default_auto_field: defaults to `django.db.models.BigAutoField`
    :type default_auto_field: str
    :param name: the name of the model, defaults to `competitions`
    :type name: str
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'competitions'
