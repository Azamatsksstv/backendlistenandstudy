from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsTeacher
from courses.models import Course
from courses.serializers.lesson import LessonCreateSerializer


class CreateLessonAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        serializer = LessonCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

