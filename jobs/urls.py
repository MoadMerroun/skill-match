from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import JobView

router = SimpleRouter()

router.register( r'jobs', JobView )

urlpatterns = router.urls

urlpatterns += [
    path( "me/applications/", JobView.as_view( { 'get': 'my_applications' } ), name = 'my_applications' ),
]
