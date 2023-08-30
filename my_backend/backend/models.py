from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
## for user
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)  

## for trainer
class FitnessProfile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)