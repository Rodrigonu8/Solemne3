from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import EjecutivoList, EjecutivoCreate, EjecutivoUpdate , EjecutivoDelete 

urlpatterns = [
    path('listar_ejecutivo/', EjecutivoList.as_view(), name="ejecutivo_list"),
    path('crear_ejecutivo/', EjecutivoCreate.as_view(), name="ejecutivo_form"),
    path('editar_ejecutivo/<int:pk>', EjecutivoUpdate.as_view(), name="ejecutivo_update"),
    path('borrar_ejecutivo/<int:pk>', EjecutivoDelete.as_view(), name="ejecutivo_borrar"),
    
]
