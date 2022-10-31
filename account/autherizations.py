from rest_framework import permissions
from parent.models import Parent
from django_server.settings import SECRET_KEY
import jwt

class ParentPermission(permissions.BasePermission):
    def has_permission(self, request):
        if request.method == 'POST':
            return True
        self.message = "you can't see other's data"
        if request.method == 'GET':
            return False
        self.message = 'request method is denied'

class ParentDetailPermission(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        sent_token = jwt.decode(request.headers.get('Jwt'), SECRET_KEY, algorithms=['HS256'])
        parent_id = Parent.objects.filter(Account__username=sent_token['username'], Account__password=sent_token['password']).first().id
        parent_to_access = Parent.objects.get(id = parent_id)
        if parent_to_access == obj:
            return True
        self.message = "you can't see other's data"
        return False