# Generated by Django 4.1.5 on 2023-12-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neostyle_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
