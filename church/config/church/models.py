from django.db import models

# Create your models here.
from staff.models import Staff
from user.models import User

class Attendance(models.Model):
    class Event(models.TextChoices):
        MASS = 'MA', _('Mass')
        BAPTISM = 'B', _('Baptism')
        MARRIAGE = 'MAR', _('Marriage')
        FUNERAL = 'F', _('Funeral')
        OTHERS = 'O', _('Others')

    user_id = models.ForeignKey(User)
    date_attended = models.DateField('date_attend', auto_now_add=True)

    event_type = models.CharField('event', max_length=3, choices=Event.choices, default=Event.MASS)
    staff_id = models.ForeignKey(Staff)

    def __str__(self):
        return f'{self.event_type}-{self.date_attended}-{self.user_id}'
