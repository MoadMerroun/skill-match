from rest_framework.serializers import ModelSerializer

from .models import Job, JobApplication

class JobSerializer( ModelSerializer ):
    class Meta:
        model = Job
        fields = ( "id", "title", "description", "recruiter" )
        read_only_fields = ( "id", "created_at", "updated_at", "recruiter" )

class JobApplicationSerializer( ModelSerializer ):
    class Meta:
        model = JobApplication
        fields = ( "id", "job", "applicant" )
        read_only_fields = ( "id", "created_at", "updated_at", "applicant" )
