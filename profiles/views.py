from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from common.permissions import IsProfileOwner, IsCandidate, IsEmployer
from .models import CandidateProfile, CompanyProfile
from .serializers import CandidateProfileSerializer, CompanyProfileSerializer

class CandidateProfileView( mixins.UpdateModelMixin, viewsets.GenericViewSet ):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [ IsAuthenticated, IsCandidate, IsProfileOwner ]

class CompanyProfileView( mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet ):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

    def get_permissions( self ):
        if self.action in [ "update", "partial_update" ]:
            permission_classes = [ IsAuthenticated, IsEmployer, IsProfileOwner ]

        else:
            permission_classes = []

        return [ permission() for permission in permission_classes ]

@api_view([ 'GET' ])
@permission_classes([ IsAuthenticated ])
def my_profile( request ):
    user = request.user

    if user.role == "candidate":
        profile = CandidateProfile.objects.get( user = user )
        serializer = CandidateProfileSerializer( profile )

    else:
        profile = CompanyProfile.objects.get( user = user )
        serializer = CompanyProfileSerializer( profile )

    return Response( serializer.data, status = status.HTTP_200_OK )
