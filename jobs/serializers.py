from rest_framework.serializers import ModelSerializer

from .models import Job

class JobSerializer( ModelSerializer ):
    class Meta:
        model = Job
        fields = ( "id", "title", "description", "recruiter" )
        read_only_fields = ( "id", "created_at", "updated_at", "recruiter" )
