from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('categoria/<int:pk>/', views.lugares_por_categoria, name='categoria'),
    path('gestion/', views.gestion, name='gestion'),
    path('gestion/lugares/nuevo/', views.lugar_crear, name='lugar_crear'),
    path('gestion/lugares/<int:pk>/editar/', views.lugar_editar, name='lugar_editar'),
]