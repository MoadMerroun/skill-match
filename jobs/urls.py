from rest_framework.routers import SimpleRouter

from .views import JobView

router = SimpleRouter()

router.register( r'jobs', JobView )

urlpatterns = router.urls
