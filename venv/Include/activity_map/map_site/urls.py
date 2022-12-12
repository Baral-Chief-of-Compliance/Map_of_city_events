from django.urls import path, include
from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics')
]