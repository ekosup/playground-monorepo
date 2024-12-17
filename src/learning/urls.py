from django.urls import path

from learning.views import index, course_detail, announcement, notification, dismiss_notification

app_name = 'learning'
urlpatterns = (
    path('', index, name='home'),
    path('course-detail/<str:pk>/', course_detail, name='course_detail'),
    path('announcement/', announcement, name='announcement'),
    path('notification/', notification, name='notification'),
    path('dismiss_notification/', dismiss_notification, name='dismiss_notification'),
)
