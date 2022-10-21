from django.urls import path
from .views import StudentsAll , StudentsParam
urlpatterns = [
    path('' , StudentsAll.as_view()),
    path('<int:id>' , StudentsParam.as_view())
]