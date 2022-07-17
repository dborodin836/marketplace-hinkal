from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.user"

    def ready(self) -> None:
        import src.apps.user.signals  # noqa
