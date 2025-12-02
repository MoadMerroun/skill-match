from rest_framework.serializers import ModelSerializer

from .models import CandidateProfile, CompanyProfile

class CandidateProfileSerializer( ModelSerializer ):
    class Meta:
        model = CandidateProfile
        fields = ( "user", "bio", "experience", "cv_url" )
        read_only_fields = ( "user", )

class CompanyProfileSerializer( ModelSerializer ):
    class Meta:
        model = CompanyProfile
        fields = ( "user", "company_name", "description", "website", "logo_url", "industry", "number_of_employees" )
        read_only_fields = ( "user", )
