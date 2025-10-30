from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')


urlpatterns = router.urls