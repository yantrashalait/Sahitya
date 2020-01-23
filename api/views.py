from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import AudioBook
from .serializers import AudioBookSerializer


class CustomAuthToken(ObtainAuthToken):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=False)
        try:
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)            
            return Response({
                'status': True,
                'msg': 'Login Successful',
                'data': {
                    'token': token.key,
                    'user_id': user.pk,
                    'username': user.username,
                    'email': user.email,
                }
                
            })
        except KeyError:
            return Response({
                'status': False,
                'msg': 'Login Failed',
            })

class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
