from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete = models.CASCADE
    )

    created_at = models.DateTimeField( auto_now_add = True )

    updated_at = models.DateTimeField( auto_now = True )

    class Meta:
        abstract = True

class CandidateProfile( Profile ):
    bio = models.TextField( default = "", blank = True )

    experience = models.PositiveIntegerField( default = 0, blank = True )

    cv_url = models.CharField( max_length=255, default = "", blank = True )

class CompanyProfile( Profile ):
    company_name = models.CharField( default = "", blank = True, max_length = 100 )

    description = models.TextField( default = "", blank = True )

    website = models.URLField( default = "", blank = True )

    logo_url = models.CharField( max_length=255, default = "", blank = True )

    industry = models.CharField( max_length = 100, default = "", blank = True )

    number_of_employees = models.PositiveIntegerField( default = 0, blank = True )
