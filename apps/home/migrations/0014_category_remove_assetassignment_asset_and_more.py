# Generated by Django 5.0.6 on 2024-06-21 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_asset_bar_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='assetassignment',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='returnedasset',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='assetassignment',
            name='department',
        ),
        migrations.RemoveField(
            model_name='department',
            name='sub_loacation',
        ),
        migrations.RemoveField(
            model_name='sublocation',
            name='main_location',
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('element_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('image', 'Image'), ('pdf', 'PDF'), ('datetime', 'Date and Time')], max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='home.element')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='home.category')),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='home.subcategory'),
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='ReturnedAsset',
        ),
        migrations.DeleteModel(
            name='AssetAssignment',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='MainLocation',
        ),
        migrations.DeleteModel(
            name='SubLocation',
        ),
    ]
