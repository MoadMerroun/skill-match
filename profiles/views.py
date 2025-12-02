from rest_framework import mixins, viewsets

from .models import CandidateProfile, CompanyProfile
from .serializers import CandidateProfileSerializer, CompanyProfileSerializer

class CandidateProfileView( mixins.UpdateModelMixin, viewsets.GenericViewSet ):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer

class CompanyProfileView( mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet ):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
