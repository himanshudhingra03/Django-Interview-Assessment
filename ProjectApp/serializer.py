from rest_framework import serializers
from .models import Employee
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
# from django.contrib import 
# from django.contrib.auth import get_user_model



class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name','username', 'email', 'date_of_joining', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        auth_employee = Employee.objects.create_user(**validated_data)
        return auth_employee
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)


    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        username=data['username']
        email = data['email']
        password = data['password']

        employee = auth.authenticate(username=username, email=email, password=password)

        if employee is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(employee)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': employee.email,
                'username': employee.username

            }

            return validation
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'email',
            'first_name',
            'last_name'
        )
