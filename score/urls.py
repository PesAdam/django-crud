from django.urls import path
from . import views
from register import views as v

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', v.register, name='register')
]