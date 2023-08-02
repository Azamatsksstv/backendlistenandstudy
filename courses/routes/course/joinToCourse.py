from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from courses.models import Course
from accounts.permissions import IsStudent


class JoinCourseAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, course_id):
        course = Course.objects.get(id=course_id)
        user = request.user
        course.students.add(user)
        return Response({'message': 'Joined the course successfully'}, status=200)
