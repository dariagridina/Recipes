# Generated by Django 3.2.8 on 2021-10-12 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211012_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientinrecipe',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.unit'),
        ),
    ]
