from django.urls import path
from accounts.routes.registration.verify import VerifyOTP
from accounts.routes.registration.register import RegisterAPI
from accounts.routes.student.myCourses import StudentMyCoursesAPIView
from accounts.routes.teacher.myCourses import TeacherMyCoursesAPIView
from accounts.routes.profile.changeUserInfo import MyProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.routes.token.CustomTokenVerifyView import CustomTokenVerifyView
from accounts.routes.teacher.TeacherList import TeacherListAPIView

urlpatterns = [
    path('accounts/register/', RegisterAPI.as_view()),
    path('accounts/verify/', VerifyOTP.as_view()),
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),

    path('my_courses/student/', StudentMyCoursesAPIView.as_view(), name='student-courses'),
    path('my_courses/teacher/', TeacherMyCoursesAPIView.as_view(), name='teacher-courses'),

    path('my_profile/', MyProfileAPIView.as_view(), name='my-profile'),

    path('teachers/', TeacherListAPIView.as_view(), name='teacher-list'),

]
