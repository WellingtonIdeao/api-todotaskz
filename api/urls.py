from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'task', TaskViewSet, basename='task')
urlpatterns = router.urls
