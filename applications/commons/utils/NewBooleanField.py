from django.db import models

class NewBooleanField(models.BooleanField):

    def get_internal_type(self):
        return "NewBooleanField"

    def db_type(self):
        return 'bit(1)'
    
  
    def to_python(self, value):
        if value in (True, False): return value
        if value in ('t', 'True', '1', '\x01'): return True  
        if value in ('f', 'False', '0', '\x00'): return False

    def get_db_prep_value(self, value, connection, prepared=False):
        return 0x01 if value else 0x00