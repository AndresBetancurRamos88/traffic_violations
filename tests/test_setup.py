from rest_framework.test import APITestCase

from apps.users.models import User

class TestSetup(APITestCase):
    def setUp(self) -> None:
        self.login_url = '/api/token/'
        self.user = User.objects.create_superuser(
            user_id = 123456,
            name = 'Daniel',
            last_name = 'Suarez',
            password = 'prueba'
        )
        self.client.force_authenticate(self.user)
