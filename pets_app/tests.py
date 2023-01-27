from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Pet


class PetTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_user1 = get_user_model().objects.create_user(username='test_user1', password='pass')
        test_user1.save()

        test_pet = Pet.objects.create(pet_name="Pico", pet_owner=test_user1, pet_mood="pesky", pet_description="Moody yet loving.")
        test_pet.save()

    def test_pet_model(self):
        pets = Pet.objects.get(id=1)
        actual_owner = str(pets.pet_owner)
        actual_name = str(pets.pet_name)
        actual_description = str(pets.pet_description)
        actual_mood = str(pets.pet_mood)
        self.assertEqual(actual_owner, 'test_user1')
        self.assertEqual(actual_name, "Pico")
        self.assertEqual(actual_mood, "pesky")
        self.assertEqual(actual_description, "Moody yet loving.")
