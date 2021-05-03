from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    class Sex(models.TextChoices):
        MAN = 'M', ('Man')
        WOMAN = 'F', ('Woman')
    sex = models.CharField(max_length=1, choices=Sex.choices, null=True)

    def __str__(self):
        return f'{self.username}'
