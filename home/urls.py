from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('timeline/', views.TimelineView.as_view(), name='timeline'),
]
