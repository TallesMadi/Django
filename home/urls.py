from django.contrib import admin
from django.urls import path
from home import views as home_view
# from . import views

app_name = 'home'

urlpatterns = [
    path('', home_view.home, name='home'),
]