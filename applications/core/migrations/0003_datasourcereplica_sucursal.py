# Generated by Django 3.2 on 2022-09-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_datasourcereplica_url_alternativa'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasourcereplica',
            name='sucursal',
            field=models.BooleanField(default=True),
        ),
    ]
