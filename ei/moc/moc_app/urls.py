from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ProjectViewSet, StudentLoginView

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', StudentLoginView.as_view(), name='student_login')
]