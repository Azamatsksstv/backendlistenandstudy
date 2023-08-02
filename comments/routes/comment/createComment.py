from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import IsStudent, IsTeacher
from comments.serializers.comment import CommentSerializer, CreateCommentSerializer
from comments.models import Comment
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from courses.models import Course, Lesson


class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStudent or IsTeacher]

    def get(self, request, course_id, lesson_id):
        course = get_object_or_404(Course, id=course_id)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
        comments = Comment.objects.filter(lesson=lesson)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, course_id, lesson_id):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, lesson_id=lesson_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
