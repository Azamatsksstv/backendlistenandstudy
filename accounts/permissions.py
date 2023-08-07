from rest_framework import permissions

import accounts.choices
from courses.models import Course
from . import choices


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == choices.UserTypeChoices.Teacher


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == choices.UserTypeChoices.Student


class IsEnrolledInCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('course_id')
        user = request.user

        if user.is_authenticated and user.courses.filter(id=course_id).exists():
            return True
        return False


class IsTeacherOfCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('course_id')
        user = request.user

        if user.is_authenticated and user.user_type == accounts.choices.UserTypeChoices.Teacher:
            course = Course.objects.get(id=course_id)
            if course.teacher == user:
                return True
        return False
