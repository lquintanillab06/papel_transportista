from django.db import models
from .managers import FolioManager
import uuid

# Create your models here.


class DataSourceReplica(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    central = models.BooleanField(default= False)
    username = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    server = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    data_base = models.CharField(max_length=255)
    activa = models.BooleanField(default= True)
    url_alternativa = models.CharField(max_length=255, blank=True, null=True)
    sucursal = models.BooleanField(default= True)

    class Meta:
        managed = True
        db_table = 'data_source_replica'

class Folio(models.Model):
    id = models.BigAutoField(primary_key=True)
    entidad = models.CharField(max_length=255, blank=True, null=True)
    folio = models.BigIntegerField()
    serie = models.CharField(max_length=255, blank=True, null=True)

    objects = FolioManager()

    class Meta:
        managed = True
        db_table = 'folio'

