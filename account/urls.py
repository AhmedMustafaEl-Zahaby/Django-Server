
from django.urls import path 
from .views import *
from parent.views import *
urlpatterns = [
    path('register/' , Register.as_view()),
    path('signin/' , Signin.as_view()),
    path('parent/' , ParentView.as_view()),
    path('parent/<int:pk>' , ParentDetailView.as_view()),
]