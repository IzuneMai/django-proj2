from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profiles', views.profile, name='profiles')
]