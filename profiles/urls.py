from rest_framework.routers import SimpleRouter

from .views import CandidateProfileView, CompanyProfileView

router = SimpleRouter()

router.register( r'candidates', CandidateProfileView )
router.register( r'companies', CompanyProfileView )

urlpatterns = router.urls
