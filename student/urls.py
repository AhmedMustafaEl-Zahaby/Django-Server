from django.urls import path
from .views import *
urlpatterns = [
    path('student/' , Student_Without.as_view()),
    path('student/<int:id>' ,StudentView.as_view()),
    path('parent/' , Parent_Without.as_view()),
    path('parent/<int:id>' ,ParentView.as_view()),
    path('subject/' , Subject_Without.as_view()),
    path('subject/<int:id>' ,SubjectView.as_view())
]