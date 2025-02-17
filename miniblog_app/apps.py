from django.apps import AppConfig


class MiniblogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miniblog_app'

    def ready(self):
        import miniblog_app.signals