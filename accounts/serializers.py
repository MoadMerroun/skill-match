from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserRegisterSerializer( serializers.ModelSerializer ):
    password = serializers.CharField( write_only = True )

    class Meta:
        model = User
        fields = ( "username", "email", "password", "role" )

    def create( request, validated_data ):
        user = User( **validated_data )
        user.set_password( validated_data[ "password" ] )
        user.save()

        return user

class UserLoginSerializer( TokenObtainPairSerializer ):
    @classmethod
    def get_token( cls, user ):
        token = super().get_token( user )
        token[ "role" ] = user.role

        return token
