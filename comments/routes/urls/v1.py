from django.urls import path
from comments.routes.comment.createComment import CommentListCreateAPIView

urlpatterns = [
    path('courses/<int:course_id>/lessons/<int:lesson_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
]
