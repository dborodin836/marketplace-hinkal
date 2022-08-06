from djoser.views import UserViewSet

from src.apps.user.api.conf import settings
from src.apps.user.models import Customer, Vendor


class CustomerViewSet(UserViewSet):
    """
    ViewSet that should be used for all action related to Customer instance.
    """
    queryset = Customer.objects.all()
    serializer_class = settings.SERIALIZERS.user


class VendorViewSet(UserViewSet):
    """
    ViewSet that should be used for all action related to Vendor instance.
    """
    queryset = Vendor.objects.all()
    serializer_class = settings.SERIALIZERS.user
