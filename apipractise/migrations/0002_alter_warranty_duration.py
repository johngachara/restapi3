# Generated by Django 4.2.7 on 2023-11-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipractise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
