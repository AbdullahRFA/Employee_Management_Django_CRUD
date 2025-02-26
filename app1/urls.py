from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('',views.HomePage,name='home'),
    path('update/',views.Update,name='update'),
]