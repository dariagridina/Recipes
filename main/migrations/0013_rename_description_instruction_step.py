# Generated by Django 3.2.8 on 2021-12-29 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_recipe_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruction',
            old_name='description',
            new_name='step',
        ),
    ]
