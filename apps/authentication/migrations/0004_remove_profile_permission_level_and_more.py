# Generated by Django 5.0.6 on 2024-07-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_permission_level'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='profile',
        #     name='permission_level',
        # ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]