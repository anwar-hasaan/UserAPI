from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import UserRegistrationSerializer
from account.models import User

class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'New User Created successful', 
                            'status': status.HTTP_201_CREATED})

        return Response({'error': serializer.errors,
                        'status': status.HTTP_400_BAD_REQUEST})
    
    def get(self, request):
        
        return Response({
            "Users": 'get method'
        })