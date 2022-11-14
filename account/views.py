from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import (UserRegistrationSerializer, UserLoginSerializer, 
                                UserProfileSerializer, UserChangePasswordSerializer,
                                SendPasswordResetEmailSerializer, UserPasswordResetSerializer, )
from django.contrib.auth import authenticate
from account.renderer import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

# genarate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user=user)
            return Response({'message': 'New User Created successful', 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user=user)
            return Response({'message': 'Login Success', 'token': token}, status=status.HTTP_200_OK)
        return Response({'errors': {'non_field_errors': 'Email or password not valid'}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            return Response({'message': 'Password Changed Successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Password reset link sent, check your email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserPasswordResetView(APIView):
#     renderer_classes = [UserRenderer]
#     def post(self, request, uid, token, format=None):
#         serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
#         if serializer.is_valid():
#             return Response({'message': 'Password Reset Successful'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This views is moved to function based cause we have frontend with this view
def UserPasswordResetView(request, uid, token):
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        data = {'password': password, 'password2': password2}
        serializer = UserPasswordResetSerializer(data=data, context={'uid': uid, 'token': token})
        if serializer.is_valid():
            return render(request, 'reset_password.html', context={"message": "Password Reset Success"})
        return render(request, 'reset_password.html', context={"errors": serializer.errors['non_field_errors'][0]})
    return render(request, 'reset_password.html')
