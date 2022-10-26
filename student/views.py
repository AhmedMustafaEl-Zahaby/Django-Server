from django.views import View
from .models import *
from .forms import StudentForm
from django.http import JsonResponse
from django.core import serializers
import json
class Student_Without(View):
    def get(self , request):
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    def post(self , request):
        try:
            form = StudentForm(data = json.loads(request.body))
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)
        
        except :
            return JsonResponse({"Message": "Unknown Format"} , status=500)

class StudentView(View):
    def get(self , request , id):
        data = serializers.serialize('json', Student.objects.get(id=id))
        return JsonResponse(json.loads(data) , safe=False)
    
    def post(self , request ,id):
        try:
            form = StudentForm(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)
        
        except :
            return JsonResponse({"Message": "Unknown Format"} , status=500)

    def put(self, request,id):
        try:
            form = StudentForm(data = json.loads(request.body) , instance=Student.objects.get(id = id))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)
        
        except :
            return JsonResponse({"Message": "Record does not exist"} , status=500)
    
    def delete(self, request,id):
        Student.objects.filter(id = id).delete()
        data = serializers.serialize('json', Student.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    

class Parent_Without(View):
    def get(self , request):
        data = serializers.serialize('json', Parent.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    def post(self , request):
        db = json.loads(request.body)
        Parent.objects.create(**db)
        data = serializers.serialize('json', Parent.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

class ParentView(View):
    def get(self, request ,*args , **kwargs):
        data = serializers.serialize('json', Parent.objects.filter(id = kwargs['id']))
        return JsonResponse(json.loads(data) , safe=False)
    
    def post(self, request,*args , **kwargs):
        db = json.loads(request.body)
        Parent.objects.create(**db)
        data = serializers.serialize('json', Parent.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    
    def put(self, request,*args , **kwargs):
        db = Parent.objects.filter(id = kwargs['id'])
        body = json.loads(request.body)
        db.update(**body)
        data = serializers.serialize('json', Parent.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

    def delete(self, request,*args , **kwargs):
        Parent.objects.filter(id = kwargs['id']).delete()
        data = serializers.serialize('json', Parent.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

class Subject_Without(View):
    def get(self , request):
        data = serializers.serialize('json', Subject.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    def post(self , request):
        db = json.loads(request.body)
        Subject.objects.create(**db)
        data = serializers.serialize('json', Subject.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

class SubjectView(View):
    def get(self, request ,*args , **kwargs):
        data = serializers.serialize('json', Subject.objects.filter(id = kwargs['id']))
        return JsonResponse(json.loads(data) , safe=False)
    
    def post(self, request,*args , **kwargs):
        db = json.loads(request.body)
        Subject.objects.create(**db)
        data = serializers.serialize('json', Subject.objects.all())
        return JsonResponse(json.loads(data) , safe=False)
    
    def put(self, request,*args , **kwargs):
        db = Subject.objects.filter(id = kwargs['id'])
        body = json.loads(request.body)
        db.update(**body)
        data = serializers.serialize('json', Subject.objects.all())
        return JsonResponse(json.loads(data) , safe=False)

    def delete(self, request,*args , **kwargs):
        Subject.objects.filter(id = kwargs['id']).delete()
        data = serializers.serialize('json', Subject.objects.all())
        return JsonResponse(json.loads(data) , safe=False)


    
