from django.shortcuts import render
from rest_framework import mixins, generics
from .serializers import ParentSerializer
from account.middlewares import Authenticate
from account.autherizations import ParentPermission, ParentDetailPermission
from .models import Parent

class ParentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    def post(self, request):
        return self.create(request)
    
    authentication_classes = [Authenticate]
    permission_classes = [ParentPermission]
    
    def get(self, request):
        return self.list(request)

class ParentDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    authentication_classes = [Authenticate]
    permission_classes = [ParentDetailPermission]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)