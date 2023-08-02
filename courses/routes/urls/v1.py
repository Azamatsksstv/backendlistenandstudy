from django.urls import path

from courses.routes.course.getAllCourse import CourseAPIView
from courses.routes.course.getCourseById import CourseDetailAPIView
from courses.routes.lesson.getLessonsByCourseId import LessonListView
from courses.routes.lesson.getLessonById import LessonDetailView
from courses.routes.course.createCourse import CreateCourseAPIView
from courses.routes.course.changeCourse import ChangeCourseAPIView
from courses.routes.course.deleteCourse import DeleteCourseAPIView
from courses.routes.lesson.createLesson import CreateLessonAPIView
from courses.routes.lesson.changeLesson import ChangeLessonAPIView
from courses.routes.lesson.deleteLesson import DeleteLessonAPIView
from courses.routes.course.joinToCourse import JoinCourseAPIView


urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='course-list'),
    path('courses/<int:course_id>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/lessons/', LessonListView.as_view(), name='lesson-list'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/', LessonDetailView.as_view(), name='lesson-detail'),

    path('courses/create/', CreateCourseAPIView.as_view(), name='create-course'),
    path('courses/<int:course_id>/change/', ChangeCourseAPIView.as_view(), name='change-course'),
    path('courses/<int:course_id>/delete/', DeleteCourseAPIView.as_view(), name='delete-course'),

    path('courses/<int:course_id>/lessons/create/', CreateLessonAPIView.as_view(), name='create-lesson'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/change/', ChangeLessonAPIView.as_view(), name='change-lesson'),
    path('courses/<int:course_id>/lessons/<int:lesson_id>/delete/', DeleteLessonAPIView.as_view(), name='delete-lesson'),

    path('courses/<int:course_id>/join/', JoinCourseAPIView.as_view(), name='join-to-course'),
]
