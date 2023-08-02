from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course
from courses.serializers.course import CourseDetailSerializer


class CourseDetailAPIView(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)
