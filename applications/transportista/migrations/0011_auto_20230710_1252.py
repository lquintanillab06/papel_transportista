# Generated by Django 3.2 on 2023-07-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportista', '0010_auto_20230706_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturistaembarques',
            name='certificado_digital',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facturistaembarques',
            name='certificado_digital_pfx',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facturistaembarques',
            name='llave_privada',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]