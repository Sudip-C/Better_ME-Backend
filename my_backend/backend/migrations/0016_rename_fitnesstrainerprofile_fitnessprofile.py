# Generated by Django 4.2.4 on 2023-08-30 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_fitnesstrainerprofile_experience'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FitnessTrainerProfile',
            new_name='FitnessProfile',
        ),
    ]
