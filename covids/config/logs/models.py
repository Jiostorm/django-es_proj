from django.db import models
from django.urls import reverse
from user.models import User
from staff.models import Staff

import datetime
# Create your models here.

class Log(models.Model):
    class CovidStatus(models.TextChoices):
        POSITIVE = 'P', ('Positive')
        NEGATIVE = 'N', ('Negative')

    class HealthStatus(models.TextChoices):
        SYMPTOMATIC = 'S', ('Symptomatic')
        ASYMPTOMATIC = 'A', ('Asymptomatic')

    covid_user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT)

    date_swabbed = models.DateField()
    covid_status = models.TextField(choices=CovidStatus.choices, default=CovidStatus.NEGATIVE)

    date_recorded = models.DateField(auto_now_add=True)
    health_status = models.TextField(choices=HealthStatus.choices, default=HealthStatus.ASYMPTOMATIC)

    @property
    def date_quarantine_ends(self):
        return self.date_swabbed + datetime.timedelta(days=14)

    def __str__(self):
        return f'{self.covid_user_id}-{self.date_swabbed}-{self.covid_status}-{self.health_status}'

    def get_absolute_url(self):
        return reverse('logs_detail', args=[str(self.id)])
