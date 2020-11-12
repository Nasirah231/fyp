from django.db import models
from django.urls import reverse

from django.core.validators import RegexValidator

class Staff(models.Model):
  name = models.CharField(max_length=200)
  IC_no = models.IntegerField
  mobile_num_regex = RegexValidator(
      regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  address = models.TextField(blank=True)
  email = models.EmailField(max_length=200)

  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})
