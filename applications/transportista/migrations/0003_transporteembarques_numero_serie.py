# Generated by Django 3.2 on 2022-09-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportista', '0002_auto_20220906_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporteembarques',
            name='numero_serie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
