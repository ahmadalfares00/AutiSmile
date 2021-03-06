from djoser.serializers import UserCreateSerializer ,UserSerializer
from rest_framework import serializers
from .models import User , AutismRecord ,AutismRecordAdult

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model =User

        fields =('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phonenumber',
                 'user_type' , 'is_superuser')


class AutismRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = AutismRecord
        fields ='__all__'


class AutismRecordAdultSerializer(serializers.ModelSerializer):

    class Meta:
        model = AutismRecordAdult
        fields ='__all__'

