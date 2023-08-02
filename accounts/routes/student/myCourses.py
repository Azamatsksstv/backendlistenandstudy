from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsStudent
from courses.serializers.course import CourseDetailSerializer


class StudentMyCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        user = request.user
        courses = user.courses.all()
        serialized_courses = CourseDetailSerializer(courses, many=True).data
        return Response({'courses': serialized_courses}, status=200)
