# Generated by Django 3.2.8 on 2021-10-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, max_length=4096, null=True),
        ),
    ]
