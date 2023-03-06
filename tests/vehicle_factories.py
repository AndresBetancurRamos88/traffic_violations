from faker import Faker
from apps.person.models import Person

faker = Faker()

class PersonFactory:
    def build_person(self):
        return{
            'name': faker.name(),
            'last_name': faker.last_name(),
            'email': faker.email
        }
    
    def create_person(self):
        return Person.objects.create(**self.build_person())