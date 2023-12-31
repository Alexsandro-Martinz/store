from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        ]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


    def update(self, instance, validate_data):
        instance.username = validate_data.get('username', instance.email)
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.email = validate_data.get('email', instance.email)
        instance.save()
        return instance
