from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import mixins
from rest_framework import generics
class StudentView(APIView):
	def get(self, request):
		data = StudentSerializer(Student.objects.all() , many = True)
		return Response(data.data)
	
	def post(self, request):
		serializer = StudentSerializer(data=request.data)
		print(serializer)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

class StudentDetailView(APIView):
	def put(self, request, id):
		serializer = StudentSerializer(data=request.data, instance=Student.objects.get(id=id))
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

	def get(self, request, id):
		try:
			serializer = StudentSerializer(Student.objects.get(id=id))
			return Response(serializer.data)
		except Student.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)

	def delete(self, request, id):
		try:
			Student.objects.get(id=id).delete()
			return Response(status=status.HTTP_200_OK)
		except Student.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)

class SubjectView(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	def get(self, request):
		queryset = self.get_queryset()
		serializer = SubjectSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = SubjectSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

class SubjectDetailView(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	def put(self, request, id):
		serializer = SubjectSerializer(data=request.data, instance=Subject.objects.get(id=id))
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

	def get(self, request, id):
		try:
			serializer = SubjectSerializer(Subject.objects.get(id=id))
			return Response(serializer.data)
		except Subject.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)

	def delete(self, request, id):
		try:
			Subject.objects.get(id=id).delete()
			return Response(status=status.HTTP_200_OK)
		except Subject.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)

class ParentView(generics.GenericAPIView, # should be there
				mixins.CreateModelMixin, # needs id
				mixins.UpdateModelMixin, # needs id
				mixins.DestroyModelMixin, # needs id
				mixins.RetrieveModelMixin, # single -> needs id
				mixins.ListModelMixin # all data
				):
	queryset = Parent.objects.all()
	serializer_class = ParentSerializer
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)