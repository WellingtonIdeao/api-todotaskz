from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(ReadOnlyModelViewSet):
    queryset = Task.objects.select_related('parent', 'category')
    serializer_class = TaskSerializer
