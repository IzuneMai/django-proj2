from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('guides', views.guides, name='guides')
]