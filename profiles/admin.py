from django.contrib import admin

from .models import CandidateProfile, CompanyProfile

admin.site.register( CandidateProfile )
admin.site.register( CompanyProfile )
