from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from profiles.models import CandidateProfile
from profiles.serializers import CandidateProfileSerializer
from .models import Job, JobApplication
from .serializers import JobSerializer

class JobView( ModelViewSet ):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create( self, serializer ):
        serializer.save( recruiter = self.request.user )

    @action( detail = True, methods = ['post'] )
    def apply( self, request, pk=None ):
        job = self.get_object()

        application, created = JobApplication.objects.get_or_create( job = job, applicant = request.user )

        if not created:
            return Response( { "detail": "You have already applied for this job." }, status = status.HTTP_200_OK )

        return Response( { "detail": "Application submitted successfully." }, status = status.HTTP_201_CREATED )

    @action( detail = True, methods = ['get'] )
    def applications( self, request, pk=None ):
        job = self.get_object()

        applications = job.applications.all()

        users = [ application.applicant for application in applications ]

        profiles = CandidateProfile.objects.filter( user__in = users )

        serializer = CandidateProfileSerializer( profiles, many = True )

        return Response( serializer.data, status = status.HTTP_200_OK )
