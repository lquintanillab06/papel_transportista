# Generated by Django 3.2 on 2022-09-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasourcereplica',
            name='url_alternativa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]