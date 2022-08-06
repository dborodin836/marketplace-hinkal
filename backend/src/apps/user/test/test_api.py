import io
from contextlib import redirect_stdout

from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.core.testing.api_clients import AdminAPIClient
from src.apps.user.models import Customer


class CustomerAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/customers/"
    detailed_url = base_url + "1/"

    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.adminClient = AdminAPIClient(  # type: ignore
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )

    def test_create_customer(self):
        user_data = {"username": "testusername", "password": "sometestpassword"}
        response = self.client.post(self.base_url, data=user_data)
        self.assertEqual(response.status_code, 201)
        print(Customer.objects.all())
        print(User.objects.all())
        # self.assertTrue(Customer.objects.get(username=user_data["username"]).exists())
