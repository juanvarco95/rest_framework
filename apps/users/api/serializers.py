from django.db.models import fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if value == '':
            raise serializers.ValidationError('Ingrese algún valor en el campo')
        return value
    
    def validate_email(self, value):
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('El nombre no puede estar en el correo')
        return value

    def validate(self, data):
        print("Validación hecha correctamente")
        return data

    def create(self, validated_data):
        print('Pasó por el create')
        return User.objects.create(**validated_data)