from django.urls import path , include
from .views import * 

urlpatterns=[
	path('student/', include([
			path('', StudentView.as_view()),
			path('<int:id>', StudentDetailView.as_view())
		])),
	path('parent/', include([
			path('<int:pk>', ParentView.as_view())
		])),
	path('subject/', include([
			path('', SubjectView.as_view()),
			path('<int:id>',SubjectDetailView.as_view())
		]))
]