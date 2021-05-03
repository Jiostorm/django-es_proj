from django.db import models
from django.urls import reverse
from staff.models import Staff
# Create your models here.

class User(models.Model):
    class Sex(models.TextChoices):
        MAN = 'M', ('Man')
        WOMAN = 'F', ('Woman')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    birthdate = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=Sex.choices, null=True)
    profession = models.CharField(max_length=50)
    
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name[0]}.'

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
