from rest_framework import serializers
from .models import Pet


# the serializer allows us to grab the data and convert into json data in the modal, it will also parse the data and
class PetSerializer(serializers.ModelSerializer):
    # need meta class to provide access to database
    class Meta:
        fields = ('id', 'pet_name', 'pet_owner', 'pet_description', 'created_at')
        model = Pet
