# Generated by Django 4.2.4 on 2023-09-01 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_rename_fitnesstrainerprofile_fitnessprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('goal', models.CharField(choices=[('Weight Loss', 'Weight Loss'), ('Muscle Gain', 'Muscle Gain'), ('Cardio Fitness', 'Cardio Fitness'), ('Other', 'Other')], max_length=20)),
                ('duration_weeks', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.fitnessprofile')),
            ],
        ),
    ]
