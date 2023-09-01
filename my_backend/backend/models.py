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

GOAL_CHOICES = [
    ('Weight Loss', 'Weight Loss'),
    ('Muscle Gain', 'Muscle Gain'),
    ('Cardio Fitness', 'Cardio Fitness'),
    ('Other', 'Other'),
]

class WorkoutPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    duration_weeks = models.PositiveIntegerField()
    description = models.TextField()

    trainer = models.ForeignKey('FitnessProfile', on_delete=models.CASCADE)  # Assumes a Trainer model exists

    def __str__(self):
        return self.plan_name
    

GOAL_CHOICES = [
    ('Weight Loss', 'Weight Loss'),
    ('Muscle Gain', 'Muscle Gain'),
    ('Balanced Diet', 'Balanced Diet'),
    ('Other', 'Other'),
]

class NutritionPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)
    duration_weeks = models.PositiveIntegerField()
    guidelines = models.TextField()

    trainer = models.ForeignKey('FitnessProfile', on_delete=models.CASCADE)  # Assumes a Trainer model exists

    def __str__(self):
        return self.plan_name