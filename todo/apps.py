from django.apps import AppConfig

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'

    def ready(self):
        import todo.signals  # Replace 'your_app_name' with the name of your app
