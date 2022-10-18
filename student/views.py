import re
from django.http import JsonResponse
from django.shortcuts import render
import json
data = []
with open('D:\Poetry\student\data.json') as files:
    data = json.load(files)
def index(request):
    if request.method == 'GET':
        return JsonResponse(data , safe=False)
    elif request.method == 'POST':
        data.append(json.loads(request.body))
        with open('D:\Poetry\student\data.json' , "w") as files: 
            json.dump(data, files)
        return JsonResponse(json.loads(request.body))

def update_delete(request,id):
    if request.method == 'PUT':
        for i in range(len(data)):
            if data[i]["id"] == id :
                data[i] = json.loads(request.body)
                break
        with open('D:\Poetry\student\data.json' , "w") as files: 
            json.dump(data, files)
        return JsonResponse(data , safe=False)

    if request.method == 'DELETE':
        for i in range(len(data)):
            if data[i]["id"] == id :
                del data[i]
                break
        with open('D:\Poetry\student\data.json' , "w") as files: 
            json.dump(data, files)
        return JsonResponse({'Message' : "Sucessful Deleting"})

