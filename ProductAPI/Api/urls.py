from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('read/', views.read, name='read'),
    path('detail/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
]