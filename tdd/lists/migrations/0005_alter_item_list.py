# Generated by Django 5.1.7 on 2025-04-04 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0004_item_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="list",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="lists.list",
            ),
        ),
    ]
