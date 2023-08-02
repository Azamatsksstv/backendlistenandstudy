from rest_framework import permissions
from . import choices


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == choices.UserTypeChoices.Teacher


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == choices.UserTypeChoices.Student


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешить GET, HEAD, OPTIONS запросы всем

        # Проверить, является ли пользователь администратором
        return request.user.is_superuser


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешить GET, HEAD, OPTIONS запросы всем

        # Проверить, является ли пользователь учителем
        return request.user.user_type == 'Teacher'


class IsStudentReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешить только GET, HEAD, OPTIONS запросы студентам
        return request.method in permissions.SAFE_METHODS and request.user.user_type == 'Student'