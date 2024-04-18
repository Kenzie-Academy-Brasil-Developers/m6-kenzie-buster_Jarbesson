from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(validators=[UniqueValidator(User.objects.all(), message="email already registered.")])
    username = serializers.CharField(max_length=50, validators=[UniqueValidator(User.objects.all(), message="username already taken.")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)
    birthdate = serializers.DateTimeField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def create(self, validated_data):
        if validated_data["is_employee"] is False:
            users = User.objects.create_user(**validated_data)
        else:
            users = User.objects.create_superuser(**validated_data)
        return users
    
