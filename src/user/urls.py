from django.urls import path

from user.views import CustomLoginView, reset_password, LogOutView, ProfileView

app_name = 'user'

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login'),
    path('reset-password/', reset_password, name='reset-password'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
)
