# Generated by Django 5.1.2 on 2024-11-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='topping',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='pizza',
            new_name='title',
        ),
    ]
