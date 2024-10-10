from rest_framework import viewsets, views, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Student, Project
from .serializers import StudentSerializer, ProjectSerializer


class StudentLoginView(views.APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            student = Student.objects.get(account=account)
            if student.password == password:
                return Response({"message": "登录成功"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "账号或密码错误"}, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"message": "此账号不存在"}, status=status.HTTP_404_NOT_FOUND)


class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'name': ['icontains'],
            'initiator': ['icontains'],
            'supervisor': ['icontains'],
            'participants': ['icontains'],
        }


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
