from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsStudent, IsTeacher

from courses.models import Lesson
from courses.serializers.lesson import LessonDetailSerializer


class LessonDetailView(APIView):
    permission_classes = [IsAuthenticated, (IsStudent | IsTeacher)]

    def get(self, request, course_id, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id, course_id=course_id)
        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)
