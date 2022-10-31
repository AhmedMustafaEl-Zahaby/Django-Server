from django.shortcuts import render
from .serializers import *
from rest_framework import generics , mixins , status
from rest_framework.response import Response
from datetime import datetime
import jwt
from django_server.settings import SECRET_KEY
from parent.models import Parent 
from tokens.models import Tokens
class Register(generics.GenericAPIView,mixins.CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def post(self , request):
        return self.create(request)

class Signin(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def put(self , request):
        try:
            [username, password, parent_id] = [request.data['username'], request.data['password'], request.data['parent']] 
            account = Account.objects.get(username=username, password=password, parent = Parent.objects.get(id=parent_id))
            token = jwt.encode({'username': username, 'password': password, 'timestamp': datetime.timestamp(datetime.now())}, SECRET_KEY, algorithm='HS256')
            newToken = {
                'token': token,
                'parent': Parent.objects.get(id=request.data['parent'])
            }
            Tokens.objects.create(**newToken)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({'message': 'Parent not registered!'}, status=status.HTTP_404_NOT_FOUND)





