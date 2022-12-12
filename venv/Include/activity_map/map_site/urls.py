from django.urls import path, include
from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('statistics_types/', views.statistics_types, name='statistics_types'),
    path('statistics_age/', views.statistics_age, name='statistics_age'),
    path('statistics_county/', views.statistics_county, name='statistics_county'),
    path('statistics_paid/', views.statistics_paid, name='statistics_paid')
]