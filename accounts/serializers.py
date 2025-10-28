from rest_framework import serializers
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
