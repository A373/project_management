from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser


# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if email is None or password is None:
        content = {
            'message': 'email or password is missing'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user = CustomUser.objects.get(email=email)
            content = {
                'user_id': user.id,
                'username': user.username,
                'mobile': user.mobile,
                'user_type': user.user_type,
                'created': user.created
            }
            return Response(content, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            context = {
                'message': 'enter valid email'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if email is None or password is None:
        content = {
            'message': 'email or password is missing'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user = CustomUser.objects.get(email=email)
            context = {
                'user_id': new_user.id,
                'user_name': new_user.username,
                'message': 'new_user has been created succesfully'

            }
            return Response(context, status=status.HTTP_200_OK, content_type='application/json')
        except user.DoesNotExist:
            context = {
                'message': 'enter valid email'
            }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
