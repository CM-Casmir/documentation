# Generated by Django 3.2.6 on 2023-09-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_label_label_label_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='label_name',
            new_name='label',
        ),
    ]
