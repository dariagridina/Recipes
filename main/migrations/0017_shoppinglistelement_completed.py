# Generated by Django 3.2.8 on 2022-01-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_shoppinglist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglistelement',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
