# Generated by Django 5.0.6 on 2024-07-23 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_department_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='document',
            name='assigned_to_email',
        ),
        migrations.RemoveField(
            model_name='document',
            name='department',
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.CreateModel(
            name='DocumentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('assigned_to', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]
