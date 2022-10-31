from rest_framework import authentication
from rest_framework import exceptions
from tokens.models import Tokens
class Authenticate(authentication.BaseAuthentication):
	def authenticate(self, request):
		token = request.headers.get('Jwt')
		for tokens in Tokens.objects.all():
			if tokens.token == token:
				return(True , None)
		raise exceptions.AuthenticationFailed("You don't have access!")