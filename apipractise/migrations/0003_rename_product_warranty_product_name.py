# Generated by Django 4.2.7 on 2023-11-19 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apipractise', '0002_alter_warranty_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warranty',
            old_name='product',
            new_name='product_name',
        ),
    ]
