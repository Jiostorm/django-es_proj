from django.db import models
from django.urls import reverse

from staff.models import Staff
from user.models import User
# Create your models here.

class Attendance(models.Model):
    class Event(models.TextChoices):
        MASS = 'MA', ('Mass')
        BAPTISM = 'B', ('Baptism')
        MARRIAGE = 'MAR', ('Marriage')
        FUNERAL = 'F', ('Funeral')
        OTHERS = 'O', ('Others')

    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    date_attended = models.DateField('date_attend', auto_now_add=True)

    event_type = models.CharField('event', max_length=3, choices=Event.choices, default=Event.MASS)
    staff_id = models.ForeignKey(Staff, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.event_type}-{self.date_attended}-{self.user_id}'

    def get_absolute_url(self):
        return reverse('attend_detail', args=[str(self.id)])
