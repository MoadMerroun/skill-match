from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import CandidateProfile, CompanyProfile
from .serializers import CandidateProfileSerializer, CompanyProfileSerializer

class CandidateProfileView( mixins.UpdateModelMixin, viewsets.GenericViewSet ):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer

class CompanyProfileView( mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet ):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

@api_view([ 'GET' ])
def my_profile( request ):
    user = request.user

    if user.role == "candidate":
        profile = CandidateProfile.objects.get( user = user )
        serializer = CandidateProfileSerializer( profile )

    else:
        profile = CompanyProfile.objects.get( user = user )
        serializer = CompanyProfileSerializer( profile )

    return Response( serializer.data, status = status.HTTP_200_OK )
