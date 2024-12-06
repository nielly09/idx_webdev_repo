from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, CommentViewSet, HeartViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'hearts', HeartViewSet, basename='heart')

urlpatterns = router.urls