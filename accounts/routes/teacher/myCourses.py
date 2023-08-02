from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsTeacher
from courses.models import Course
from courses.serializers.course import CourseDetailSerializer


class TeacherMyCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        user = request.user
        courses = Course.objects.filter(teacher=user)
        serialized_courses = CourseDetailSerializer(courses, many=True).data
        return Response({'courses': serialized_courses}, status=200)
