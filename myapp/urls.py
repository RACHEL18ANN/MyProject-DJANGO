from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, post_list

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Ensure urlpatterns is correctly defined
urlpatterns = [
    path('api/posts/', post_list, name='post-list'),
    path('api/', include(router.urls)), 
]


if not urlpatterns:
    raise ImportError("The urlpatterns list is empty. Check for circular imports or misconfigurations.")