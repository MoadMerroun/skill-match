# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from profiles.models import CandidateProfile, CompanyProfile
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer

class RegisterView( CreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [ AllowAny ]

    def create( self, request, *args, **kwargs ):
        serializer = self.get_serializer( data = request.data )
        serializer.is_valid( raise_exception = True )

        user = serializer.save()

        if user.role == "candidate":
            CandidateProfile.objects.create( user = user )

        else:
            CompanyProfile.objects.create( user = user )

        refresh_token = RefreshToken.for_user( user )
        refresh_token[ "role" ] = user.role

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            },
            "access": str( refresh_token.access_token ),
            "refresh": str( refresh_token )
        }, status = status.HTTP_201_CREATED )

class LoginView( TokenObtainPairView ):
    serializer_class = UserLoginSerializer
