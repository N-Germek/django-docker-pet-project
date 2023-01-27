from django.db import models
from django.contrib.auth import get_user_model


class Pet(models.Model):
    pet_name = models.CharField(max_length=30)
    pet_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pet_description = models.TextField()
    pet_mood = models.TextField(default="happy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pet_name

    class Meta:
        verbose_name_plural = 'Pet'
