from django.urls import path
from .views import IndexView, YacimientosView, PerforacionView, ProduccionView, PostView

# Aqui se mapea lo que este dentro de url blog
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('yacimientos', YacimientosView.as_view(), name='yacimientos'),
    path('perforación', PerforacionView.as_view(), name='perforacion'),
    path('producción', ProduccionView.as_view(), name='produccion'),
    path('<str:categoria>/<str:slug>/', PostView.as_view(), name='post'),
]
