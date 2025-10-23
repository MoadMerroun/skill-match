# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegisterSerializer

class RegisterView( CreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [ AllowAny ]
