# Generated by Django 5.1.2 on 2025-01-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippets',
            new_name='Snippet',
        ),
    ]