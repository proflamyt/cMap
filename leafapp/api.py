from rest_framework import routers

from leafapp.viewset import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"marks", MarkerViewSet)

urlpatterns = router.urls