from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('',views.HomePage,name='home'),
    path('<int:id>/',views.Update,name='update'),
    path('delete/<int:id>/',views.Delete_record,name='delete'),
]