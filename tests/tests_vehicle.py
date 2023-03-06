import pdb
from faker import Faker
from rest_framework import status
import responses

from tests.test_setup import TestSetup
from tests.vehicle_factories import PersonFactory


faker = Faker()

class VehicleTestCase(TestSetup):
    url = '/vehicle/'


    def test_vehicle_create(self):
        person = PersonFactory().create_person()
        response = self.client.post(
            self.url,
            {
            "licence_plate": faker.license_plate(),
            "comment": "Test",
            "person": person.id
            },
            format = 'json',  
        )
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_create_not_found(self):
        response = self.client.post(
            self.url,
            {
            "licence_plate": faker.license_plate(),
            "comment": "Test",
            },
            format = 'json',  
        )
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)