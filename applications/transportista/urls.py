from django.urls import path
from . import views 

urlpatterns = [
    path('api/embarques_pendientes', views.EmbarquesPendientes.as_view() ),
    path('api/buscar_embarque_pendiente', views.BuscarEmbarquePendiente.as_view() ),
    path('api/embarques_cancelados', views.EmbarquesCancelados.as_view() ),
    path('api/buscar_embarque_cancelado', views.BuscarEmbarqueCancelado.as_view() ),
    path('api/embarques_facturados', views.EmbarquesFacturados.as_view() ),
    path('api/buscar_embarque_facturado', views.BuscarEmbarqueFacturado.as_view() ),
    path('api/generarCfdiCartaPorte', views.generarCfdiCartaPorte),
    path('api/generarCfdiCartaPorte2',views.GenerarCfdiView.as_view(), name='cfdi'),
    path('api/getXmlDict', views.get_xml_dictionary), 
    path('api/cancelarEmbarque', views.cancelar_embarque),
    path('api/usuario_sucursal', views.get_usuario_sucursal),
    path('api/imprimirCfdiCartaPorte', views.imprimir_cfdi_cartaporte),
    path('api/enviar_email', views.enviar_email),
    path('test_views/<prueba>/<otro>',views.TestViews.as_view()),
    path('api/cfdi_cancelados', views.CfdiCancelados.as_view() ),
    path('api/cancelar_cfdi', views.cancelar_cfdi, name='cancelar_cfdi' ),
    path("api/get_key/<str:facturista_id>",views.get_key, name="get_key"),
    path("api/get_cert/<str:facturista_id>",views.get_cert, name="get_cert"),
    path("api/get_pfx/<str:facturista_id>",views.get_pfx, name="get_pfx"),
    path("api/get_numero_certificado/<str:facturista_id>",views.get_numero_certificado, name="get_numero_certificado"),
    path("api/set_numero_certificado/<str:facturista_id>",views.set_numero_certificado, name="set_numero_certificado"),
    path("api/upload_cert_view/<str:facturista_id>/<filename>",views.UploadCertView.as_view(),name="upload_cert_view"),
    path("api/upload_key_view/<str:facturista_id>/<filename>",views.UploadKeyView.as_view(),name="upload_key_view"),
    path("api/upload_pfx_view/<str:facturista_id>/<filename>",views.UploadPfxView.as_view(),name="upload_pfx_view"),
]