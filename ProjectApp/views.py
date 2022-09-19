from django.shortcuts import render
from .serializer import UserRegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from rest_framework.response import Response

from . serializer import UserRegistrationSerializer, UserLoginSerializer, UserListSerializer
# Create your views here.
class UserRegistrationView(CreateAPIView):
    """
    Create a user with the given credentials and assign role of Librarian or Member based on value of is_librarian or is_member.
    """
    queryset = Employee.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )


# class AuthUserLoginView(ListAPIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny, )


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email']
                    # 'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)

class UserListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)


    

