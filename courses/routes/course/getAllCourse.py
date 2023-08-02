from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import IsAdminOrReadOnly
from courses.models import Course
from courses.serializers.course import CourseListSerializer


class CourseAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data)
