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
]