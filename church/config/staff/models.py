from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Staff(AbstractUser):
    sex = models.CharField(max_length=10, null=True, blank=True)
