# Generated by Django 4.1.4 on 2022-12-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_immobile_type_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='immobile',
            name='is_locate',
            field=models.BooleanField(default=False),
        ),
    ]
