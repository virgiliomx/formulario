# Generated by Django 4.2.2 on 2023-07-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='slug',
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
    ]
