from .views import studentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', studentViewSet, basename='student')
urlpatterns = router.urls