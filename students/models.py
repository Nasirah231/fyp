from django.db import models
from django.urls import reverse

from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    LEVEL = [
        ('fskm', 'FSKM'),
        ('fpa', 'FPA')
    ]

    PTPTN = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    HEALTH = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    PROBLEMS = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    registration_number = models.IntegerField(unique=True)
    level = models.CharField(max_length=10, choices=LEVEL)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER)
    IC_no = models.IntegerField
    matric_no = models.IntegerField
    address = models.TextField(blank=True)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    email = models.EmailField(max_length=200)
    scholarship = models.CharField(max_length=200, choices=PTPTN)
    family_income = models.IntegerField
    family_dependent = models.IntegerField
    health = models.CharField(max_length=10, choices=HEALTH)
    family_problems = models.CharField(max_length=10, choices=PROBLEMS)

    def __str__(self):
        return f'{self.name} ({self.registration_number})'
        
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk':self.pk})

    

    
