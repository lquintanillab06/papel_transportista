from django.db import models

# Create your models here.
from django.db import models
import uuid
from .managers import EmbarquesManager

#from .managers import EmbarquesManager, EnvioDetManager, EnviosManager, FacturistaEmbarquesManager, InstruccionDeEnvioManager

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(unique=True, max_length=13)
    email = models.CharField(max_length=255, blank=True, null=True)
    forma_de_pago = models.CharField(max_length=255, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    regimen_fiscal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'


class Embarque(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    documento = models.IntegerField(blank=True, null=True)
    operador = models.ForeignKey('Operador', models.DO_NOTHING)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    facturista = models.ForeignKey('FacturistaEmbarques', models.DO_NOTHING)
    fecha = models.DateField()
    or_fecha_hora_salida = models.DateTimeField(blank=True, null=True)
    regreso = models.DateTimeField(blank=True, null=True)
    cerrado = models.DateTimeField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    importe_comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    facturado = models.DateTimeField(blank=True, null=True)
    cancelado = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    empleado = models.CharField(max_length=255, blank=True, null=True)
    sx = models.CharField(unique=True, max_length=255, blank=True, null=True)
    cp_version = models.CharField(max_length=20, blank=True, null=True)
    cp_transp_internac = models.CharField(max_length=20, blank=True, null=True)
    cp_total_distancia_recorrida = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    or_origen = models.CharField(max_length=20, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    or_rfc_remitente = models.CharField(max_length=255)
    or_cliente_remitente = models.CharField(max_length=255, blank=True, null=True)
    me_num_total_mercancias = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    me_unidad_peso = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()

    objects = EmbarquesManager()

    class Meta:
        managed = True
        db_table = 'embarques'


class Envio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    embarque = models.ForeignKey(Embarque, models.DO_NOTHING, related_name='envios')
    sucursal = models.CharField(max_length=255)
    operador = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    entidad = models.CharField(max_length=255)
    fecha_documento = models.DateTimeField()
    documento = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=255)
    forma_pago = models.CharField(max_length=255, blank=True, null=True)
    pagado = models.BooleanField(default= False)
    parcial = models.BooleanField(default= False)
    paquetes = models.IntegerField(blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    total_documento = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    valor_caja = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    maniobra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    importe_comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    comision_por_tonelada = models.BooleanField(default= False) 
    comentario_comision = models.CharField(max_length=255, blank=True, null=True)
    salida = models.DateTimeField(blank=True, null=True)
    arribo = models.DateTimeField(blank=True, null=True)
    arribo_latitud = models.DecimalField(max_digits=19, decimal_places=2)
    arribo_longitud = models.DecimalField(max_digits=19, decimal_places=2)
    recepcion = models.DateTimeField(blank=True, null=True)
    recepcion_latitud = models.DecimalField(max_digits=19, decimal_places=2)
    recepcion_longitud = models.DecimalField(max_digits=19, decimal_places=2)
    regreso = models.DateTimeField(blank=True, null=True)
    fecha_comision = models.DateTimeField(blank=True, null=True)
    recibio = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    reporto_nombre = models.CharField(max_length=255, blank=True, null=True)
    reporto_puesto = models.CharField(max_length=255, blank=True, null=True)
    entregado = models.BooleanField(default= False)  
    completo = models.BooleanField(default= False) 
    matratado = models.BooleanField(default= False)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    impreso = models.BooleanField(default= False)
    cortado = models.BooleanField(default= False)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    callcenter = models.CharField(max_length=255, blank=True, null=True)
    callcenter_version = models.IntegerField(blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)
    manual = models.BooleanField(default= False)
    facturista = models.ForeignKey('FacturistaEmbarques', models.DO_NOTHING)
    sx = models.CharField(unique=True, max_length=255, blank=True, null=True)
    de_destino = models.CharField(max_length=20, blank=True, null=True)
    de_rfc_destinatario = models.CharField(max_length=255, blank=True, null=True)
    de_destinatario = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()

    # objects = EnviosManager()

    class Meta:
        managed = True
        db_table = 'envio'


class EnvioDet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    envio = models.ForeignKey(Envio, models.DO_NOTHING, related_name='enviosdet')
    facturista = models.ForeignKey('FacturistaEmbarques', models.DO_NOTHING)
    producto_id = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    me_descripcion = models.CharField(max_length=255)
    me_kilos = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=3)
    me_cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_entrega = models.CharField(max_length=255, blank=True, null=True)
    entregado = models.BooleanField(default= False)
    completo = models.BooleanField(default= False)
    matratado = models.BooleanField(default= False)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    impreso = models.BooleanField(default= False)
    cortado = models.BooleanField(default= False)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField()
    sx = models.CharField(unique=True, max_length=255, blank=True, null=True)
    me_bienes_transp = models.CharField(max_length=255, blank=True, null=True)
    me_clave_unidad = models.CharField(max_length=255, blank=True, null=True)
    me_unidad = models.CharField(max_length=255, blank=True, null=True)
    me_material_peligroso = models.CharField(max_length=2, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()

    # objects = EnvioDetManager()

    class Meta:
        managed = True
        db_table = 'envio_det'



class FacturistaEmbarques(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(unique=True, max_length=13)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    descuent_en_prestamo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    orden = models.BigIntegerField()
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    regimen = models.CharField(max_length=300)
    llave_privada = models.BinaryField(blank=True, null=True)
    numero_de_certificado = models.CharField(max_length=20, blank=True, null=True)
    certificado_digital = models.BinaryField(blank=True, null=True)
    certificado_digital_pfx = models.BinaryField(blank=True, null=True)
    clave = models.CharField(unique=True, max_length=15)
    password_pac = models.CharField(max_length=255, blank=True, null=True)
    password_pfx = models.CharField(max_length=255, blank=True, null=True)
    timbrado_de_prueba = models.BooleanField(default= True)
    usuario_pac = models.CharField(max_length=255, blank=True, null=True)
    version_de_cfdi = models.CharField(max_length=3)
    regimen_clave_sat = models.CharField(max_length=20, blank=True, null=True)
    sx = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    serie_cfdi =  models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    regimen_fiscal = models.CharField(max_length=255, blank=True, null=True)

    # objects = FacturistaEmbarquesManager()

    class Meta:
        managed = True
        db_table = 'facturista_embarques'


class InstruccionDeEnvio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    envio = models.ForeignKey(Envio, models.DO_NOTHING)
    facturista = models.ForeignKey(FacturistaEmbarques, models.DO_NOTHING, null=True)
    transporte = models.ForeignKey('TransporteForaneo', models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    horario = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    fecha_de_entrega = models.DateTimeField(blank=True, null=True)
    sx = models.CharField(unique=True, max_length=255, blank=True, null=True)
    ub_distancia_recorrida = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    de_fecha_hora_progllegada = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()

    # objects = InstruccionDeEnvioManager()

    class Meta:
        managed = True
        db_table = 'instruccion_de_envio'


class Operador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default= True)
    cve_transporte = models.CharField(max_length=255)
    rfc = models.CharField(unique=True, max_length=13)
    num_licencia = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    facturista = models.ForeignKey(FacturistaEmbarques, models.DO_NOTHING)
    transporte = models.ForeignKey('TransporteEmbarques', models.DO_NOTHING)
    sx = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'operador'


class Propietario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default= True)
    facturista = models.ForeignKey(FacturistaEmbarques, models.DO_NOTHING)
    rfc = models.CharField(unique=True, max_length=13)
    nombre = models.CharField(max_length=255)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'propietario'


class Sucursal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default= True)
    clave = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    almacen = models.BooleanField(default= False)
    db_url = models.CharField(max_length=255, blank=True, null=True)
    sx = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    or_estado =  models.CharField(max_length=100, blank=True, null=True)
    or_municipio =  models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sucursal'


class TransporteEmbarques(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default= True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    iv_anio_modelo = models.CharField(max_length=255, blank=True, null=True)
    iv_config_vehicular = models.CharField(max_length=255, blank=True, null=True)
    iv_placa_vm = models.CharField(unique=True, max_length=255)
    af_perm_sct = models.CharField(max_length=255, blank=True, null=True)
    af_num_permiso_sct = models.CharField(max_length=255, blank=True, null=True)
    af_nombre_aseg = models.CharField(max_length=255, blank=True, null=True)
    af_num_poliza_seguro = models.CharField(max_length=255, blank=True, null=True)
    poliza_vigencia = models.DateField(blank=True, null=True)
    facturista = models.ForeignKey(FacturistaEmbarques, models.DO_NOTHING)
    propietario = models.ForeignKey(Propietario, models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    numero_serie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transporte_embarques'


class TransporteForaneo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    telefono3 = models.CharField(max_length=255, blank=True, null=True)
    telefono2 = models.CharField(max_length=255, blank=True, null=True)
    telefono1 = models.CharField(max_length=255, blank=True, null=True)
    sucursal = models.CharField(max_length=255, blank=True, null=True)
    sx = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'transporte_foraneo'


class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activo = models.BooleanField(default= True)
    clave = models.CharField(unique=True, max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    de_linea = models.BooleanField(default= True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    inventariable = models.BooleanField(default= True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    nacional = models.BooleanField(default= True)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    sw2 = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=10)
    producto_sat = models.ForeignKey('ProductoSat', models.DO_NOTHING, blank=True, null=True)
    unidad_sat = models.ForeignKey('UnidadSat', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producto'


class ProductoSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_prod_serv = models.CharField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'producto_sat'

class UnidadSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    unidad_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unidad_sat'


class Cfdi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField()
    tipo_de_comprobante = models.CharField(max_length=1)
    origen = models.CharField(max_length=255)
    serie = models.CharField(max_length=30, blank=True, null=True)
    folio = models.CharField(max_length=30, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    emisor_rfc = models.CharField(max_length=13)
    emisor = models.CharField(max_length=255)
    file_name = models.CharField(max_length=150)
    receptor_rfc = models.CharField(max_length=13)
    receptor = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.IntegerField(blank=True, null=True)
    cancel_status = models.CharField(max_length=255, blank=True, null=True)
    comentario_cancel = models.CharField(max_length=255, blank=True, null=True)
    status_code = models.CharField(max_length=200, blank=True, null=True)
    is_cancelable = models.CharField(max_length=255, blank=True, null=True)
    enviado = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    version_cfdi = models.CharField(max_length=3)
    xml = models.TextField()
    uuid_relacionado = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_relacion = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField()
    cadena =  models.CharField(max_length=1000, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'cfdi'


class CodigosPostalesMX(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     estado = models.CharField(max_length=255, blank=True, null=True)
     asentamiento = models.CharField(max_length=255, blank=True, null=True)
     codigo = models.CharField(max_length=255, blank=True, null=True)
     colonia = models.CharField(max_length=255, blank=True, null=True)
     municipio = models.CharField(max_length=255, blank=True, null=True)
     ciudad = models.CharField(max_length=255, blank=True, null=True)
     municipio_sat = models.CharField(max_length=255, blank=True, null=True)
     localidad_sat = models.CharField(max_length=255, blank=True, null=True)
     codigo_sat = models.CharField(max_length=255, blank=True, null=True)
     estado_sat = models.CharField(max_length=255, blank=True, null=True)

     class Meta:
        managed = False
        db_table = 'codigos_postales_mx'