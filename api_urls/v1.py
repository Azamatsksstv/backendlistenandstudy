from django.urls import path, include


urlpatterns = [
    path('', include('accounts.routes.urls.v1')),
    path('dashboard/', include('courses.routes.urls.v1')),
    path('dashboard/', include('comments.routes.urls.v1'))
]
