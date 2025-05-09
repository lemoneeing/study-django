# Generated by Django 5.1.2 on 2024-11-06 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('career', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.chef')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.pizza')),
                ('related_topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.topping')),
            ],
            options={
                'db_table': 'restaurant_recipe',
            },
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(through='restaurant.Recipe', to='restaurant.topping'),
        ),
    ]
