# Generated by Django 3.2.6 on 2023-09-04 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('data_type', models.CharField(choices=[('varchar', 'Varchar'), ('integer', 'Integer'), ('date', 'Date'), ('timestamp', 'Timestamp')], max_length=20)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='Column',
        ),
    ]
