from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'email', 'username', 'first_name', 'password']

    def create(self, validated_date):
        password = validated_date.pop('password', None)
        instance = self.Meta.model(**validated_date)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'avatar',
                  'description', 'website', 'instagram', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'avatar',
                  'description', 'website', 'instagram']
