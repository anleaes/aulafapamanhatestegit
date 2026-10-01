from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='categorias')

urlpatterns = [
    path('adicionar/', views.add_category, name='add_category'),
    path('', include(router.urls) )
]

