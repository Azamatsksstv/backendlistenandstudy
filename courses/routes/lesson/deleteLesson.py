from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from accounts.permissions import IsTeacherOfCourse
from courses.models import Course, Lesson
import os


class DeleteLessonAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherOfCourse]

    def delete(self, request, course_id, lesson_id):
        course = get_object_or_404(Course, id=course_id)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)

        if lesson.audio:
            audio_path = lesson.audio.path
            if os.path.exists(audio_path):
                os.remove(audio_path)

        lesson.delete()
        return Response({'message': 'Lesson deleted successfully'}, status=204)