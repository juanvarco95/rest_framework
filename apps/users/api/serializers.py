from django.db.models import fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User



    def to_representation(self, instance):
        return {
            'id' : instance['id'],
            'nombre_usuario' : instance['name'],
            'correo_electrónico' : instance['email'],
            'contraseña' : instance['password'],
        }



