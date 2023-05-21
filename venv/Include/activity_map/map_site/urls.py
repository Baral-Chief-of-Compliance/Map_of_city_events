from django.urls import path, include
from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('', views.statistics_types, name='statistics_types'),
    path('statistics_age/', views.statistics_age, name='statistics_age'),
    path('statistics_county/', views.statistics_county, name='statistics_county'),
    path('statistics_paid/', views.statistics_paid, name='statistics_paid'),
    path('statistics_date/', views.statistics_date, name='statistics_date'),
    path('statistics_date/<str:start_year>-<str:start_month>-<str:start_day>-<str:end_year>-<str:end_month>-<str:end_day>', views.statistics_interval),
    path('all_events/', views.all_events, name='all_events'),
    path('filter_events/', views.use_filter, name='filter_events'),
    path('categories_events/',  views.categories_filter, name='categories_filter'),
    path('all_events/<int:id>', views.inf_about_event, name='inf_about_event')
]