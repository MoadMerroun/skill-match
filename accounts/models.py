from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ( "candidate", "Candidate" ),
    ( "employer", "Employer" )
)

class User( AbstractUser ):
    role = models.CharField( max_length = 20, choices = ROLE_CHOICES )
    email = models.EmailField( unique = True )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "username" ]
