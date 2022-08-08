from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    # retrieve, in a single batch, related objects of reverse relationship
    queryset = Category.objects.prefetch_related('tasks')
    serializer_class = CategorySerializer


class TaskViewSet(ReadOnlyModelViewSet):
    # recursively prepopulates the queryset cache the all one-to-many relationships
    queryset = Task.objects.select_related('parent', 'category')
    serializer_class = TaskSerializer
