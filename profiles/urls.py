from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import CandidateProfileView, CompanyProfileView, my_profile

router = SimpleRouter()

router.register( r'candidates', CandidateProfileView )
router.register( r'companies', CompanyProfileView )

urlpatterns = router.urls

urlpatterns += [
    path( 'me/profile/', my_profile, name = 'my_profile' ),
]
