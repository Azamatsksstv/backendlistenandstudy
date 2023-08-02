from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course
from courses.serializers.lesson import LessonSerializer


class LessonListView(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        lessons = course.lessons.all()
        serialized_lessons = LessonSerializer(lessons, many=True).data
        return Response({'lessons': serialized_lessons})
