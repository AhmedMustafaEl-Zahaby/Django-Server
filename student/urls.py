import imp
from turtle import update
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index),
    path('<int:id>' , views.update_delete)
]