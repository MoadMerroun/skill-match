from rest_framework.viewsets import ModelViewSet

from .models import Job
from .serializers import JobSerializer

class JobView( ModelViewSet ):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create( self, serializer ):
        serializer.save( recruiter = self.request.user )
