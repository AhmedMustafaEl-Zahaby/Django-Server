from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Student
from django.core import serializers
import json
# Create your views here.

class StudentsAll(View):
    def get(self, request):
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    
    def post(self, request):
        db = json.loads(request.body)
        Student.objects.create(**db)
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

class StudentsParam(View):
    def get(self, request ,*args , **kwargs):
        data = serializers.serialize('json', Student.objects.filter(id = kwargs['id']))
        return JsonResponse(json.loads(data) , safe=False)
    
    def post(self, request,*args , **kwargs):
        db = json.loads(request.body)
        Student.objects.create(**db)
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    
    def put(self, request,*args , **kwargs):
        db = Student.objects.filter(id = kwargs['id'])
        body = json.loads(request.body)
        db.update(**body)
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

    def delete(self, request,*args , **kwargs):
        Student.objects.filter(id = kwargs['id']).delete()
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
