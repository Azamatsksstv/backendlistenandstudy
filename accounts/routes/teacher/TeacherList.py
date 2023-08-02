from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers.user import UserInfoSerializer
from accounts import choices
from rest_framework.permissions import IsAdminUser


class TeacherListAPIView(APIView):
    # permission_classes = IsAdminUser

    def get(self, request):
        teachers = User.objects.filter(user_type=choices.UserTypeChoices.Teacher)
        serializer = UserInfoSerializer(teachers, many=True)
        return Response(serializer.data)
