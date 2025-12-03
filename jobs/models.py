from django.db import models

# Create your models here.
class Job( models.Model ):
    title = models.CharField( max_length = 20 )
    description = models.CharField( max_length = 200 )
    recruiter = models.ForeignKey( "accounts.User", on_delete = models.CASCADE, related_name="jobs", limit_choices_to={ "role": "employer" } )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
