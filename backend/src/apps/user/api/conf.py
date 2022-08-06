from django.apps import apps
from django.conf import settings as django_settings
from django.utils.functional import LazyObject
from djoser.conf import ObjDict, Settings

DJOSER_SETTINGS_NAMESPACE = "DJOSER"

auth_module, user_model = django_settings.AUTH_USER_MODEL.rsplit(".", 1)

User = apps.get_model(auth_module, user_model)

default_settings = {
    "USER_ID_FIELD": User._meta.pk.name,
    "LOGIN_FIELD": User.USERNAME_FIELD,
    "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": False,
    "USER_CREATE_PASSWORD_RETYPE": False,
    "SET_PASSWORD_RETYPE": False,
    "PASSWORD_RESET_CONFIRM_RETYPE": False,
    "SET_USERNAME_RETYPE": False,
    "USERNAME_RESET_CONFIRM_RETYPE": False,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": False,
    "USERNAME_RESET_SHOW_EMAIL_NOT_FOUND": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": False,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,
    "TOKEN_MODEL": "rest_framework.authtoken.models.Token",
    "SERIALIZERS": ObjDict(
        {
            "activation": "src.apps.user.serializers.ActivationSerializer",
            "password_reset": "src.apps.user.serializers.SendEmailResetSerializer",
            "password_reset_confirm": "src.apps.user.serializers.PasswordResetConfirmSerializer",
            "password_reset_confirm_retype": "src.apps.user.serializers.PasswordResetConfirmRetypeSerializer",
            "set_password": "src.apps.user.serializers.SetPasswordSerializer",
            "set_password_retype": "src.apps.user.serializers.SetPasswordRetypeSerializer",
            "set_username": "src.apps.user.serializers.SetUsernameSerializer",
            "set_username_retype": "src.apps.user.serializers.SetUsernameRetypeSerializer",
            "username_reset": "src.apps.user.serializers.SendEmailResetSerializer",
            "username_reset_confirm": "src.apps.user.serializers.UsernameResetConfirmSerializer",
            "username_reset_confirm_retype": "src.apps.user.serializers.UsernameResetConfirmRetypeSerializer",
            "user_create": "src.apps.user.serializers.UserCreateSerializer",
            "user_create_password_retype": "src.apps.user.serializers.UserCreatePasswordRetypeSerializer",
            "user_delete": "src.apps.user.serializers.UserDeleteSerializer",
            "user": "src.apps.user.serializers.UserSerializer",
            "current_user": "src.apps.user.serializers.UserSerializer",
            "token": "src.apps.user.serializers.TokenSerializer",
            "token_create": "src.apps.user.serializers.TokenCreateSerializer",
        }
    ),
    "EMAIL": ObjDict(
        {
            "activation": "djoser.email.ActivationEmail",
            "confirmation": "djoser.email.ConfirmationEmail",
            "password_reset": "djoser.email.PasswordResetEmail",
            "password_changed_confirmation": "djoser.email.PasswordChangedConfirmationEmail",
            "username_changed_confirmation": "djoser.email.UsernameChangedConfirmationEmail",
            "username_reset": "djoser.email.UsernameResetEmail",
        }
    ),
    "CONSTANTS": ObjDict({"messages": "djoser.constants.Messages"}),
    "LOGOUT_ON_PASSWORD_CHANGE": False,
    "CREATE_SESSION_ON_LOGIN": False,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [],
    "HIDE_USERS": True,
    "PERMISSIONS": ObjDict(
        {
            "activation": ["rest_framework.permissions.AllowAny"],
            "password_reset": ["rest_framework.permissions.AllowAny"],
            "password_reset_confirm": ["rest_framework.permissions.AllowAny"],
            "set_password": ["djoser.permissions.CurrentUserOrAdmin"],
            "username_reset": ["rest_framework.permissions.AllowAny"],
            "username_reset_confirm": ["rest_framework.permissions.AllowAny"],
            "set_username": ["djoser.permissions.CurrentUserOrAdmin"],
            "user_create": ["rest_framework.permissions.AllowAny"],
            "user_delete": ["djoser.permissions.CurrentUserOrAdmin"],
            "user": ["djoser.permissions.CurrentUserOrAdmin"],
            "user_list": ["djoser.permissions.CurrentUserOrAdmin"],
            "token_create": ["rest_framework.permissions.AllowAny"],
            "token_destroy": ["rest_framework.permissions.IsAuthenticated"],
        }
    ),
}


class LazySettings(LazyObject):
    def _setup(self, explicit_overriden_settings=None):
        self._wrapped = Settings(default_settings, explicit_overriden_settings)


settings = LazySettings()
