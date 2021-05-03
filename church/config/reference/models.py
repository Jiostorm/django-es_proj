from django.db import models
from django.urls import reverse

from user.models import User
from staff.models import Staff
# Create your models here.

class CovidReference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT)
    covid_reference_id = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.covid_reference_id

    def get_absolute_url(self):
        return reverse('ref_detail', args=[str(self.user_id)])
