# Generated by Django 3.2 on 2022-09-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cfdi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('tipo_de_comprobante', models.CharField(max_length=1)),
                ('origen', models.CharField(max_length=12)),
                ('serie', models.CharField(blank=True, max_length=30, null=True)),
                ('folio', models.CharField(blank=True, max_length=30, null=True)),
                ('uuid', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('emisor_rfc', models.CharField(max_length=13)),
                ('emisor', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=150)),
                ('receptor_rfc', models.CharField(max_length=13)),
                ('receptor', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('cancelado', models.IntegerField(blank=True, null=True)),
                ('cancel_status', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario_cancel', models.CharField(blank=True, max_length=255, null=True)),
                ('status_code', models.CharField(blank=True, max_length=200, null=True)),
                ('is_cancelable', models.CharField(blank=True, max_length=255, null=True)),
                ('enviado', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
                ('version_cfdi', models.CharField(max_length=3)),
                ('xml', models.TextField()),
                ('uuid_relacionado', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_de_relacion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('create_user', models.CharField(blank=True, max_length=255, null=True)),
                ('update_user', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.BigIntegerField()),
                ('cadena', models.TextField()),
            ],
            options={
                'db_table': 'cfdi',
                'managed': False,
            },
        ),
    ]
