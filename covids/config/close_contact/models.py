from django.db import models
from django.urls import reverse

from user.models import User
from staff.models import Staff

import datetime
# Create your models here.

class CloseContact(models.Model):
    covid_user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='covid_user_ID')
    close_user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='close_user_ID')
    date_recorded = models.DateField(auto_now_add=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT, null=True)

    @property
    def date_quarantine_ends(self):
        return self.date_recorded + datetime.timedelta(days=14)

    def __str__(self):
        return f'{self.covid_user_id}-{self.close_user_id}'

    def get_absolute_url(self):
        return reverse('cc_detail', args=[str(self.id)])
