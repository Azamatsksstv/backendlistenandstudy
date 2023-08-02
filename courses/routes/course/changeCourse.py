from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from courses.models import Course
from courses.serializers.course import CourseCreateSerializer
from accounts.permissions import IsTeacher


class ChangeCourseAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser or IsTeacher]

    def put(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        serializer = CourseCreateSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
