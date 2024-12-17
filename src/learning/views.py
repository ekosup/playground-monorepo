from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from learning.models import Course


@login_required(login_url='user:login')
def index(request):
    context = {
        'title': 'Dashboard',
        'is_home': True,
        'average_score': 80,
        'total': 100,
        'user_courses': Course.objects.filter(students__user=request.user)
    }
    return render(request, 'learning/pages/dashboard.html', context=context)


def announcement(request):
    context = {
        'title': 'Announcement',
        'detail': 'Update password for your account',
    }
    return render(request, 'asset/components/announcement.html', context)


def notification(request):
    if messages.get_messages(request):
        message = [m.message for m in messages.get_messages(request)]
    else:
        message = ""
    return render(request, 'asset/components/notification.html', {'messages': message})


def dismiss_notification(request):
    # You can add logic here to handle the dismissal of the notification on the server side.
    # For example, you could mark the notification as read in the database.

    # Return an empty HTTP response. The notification is already removed on the client side by htmx.
    return HttpResponse('')


@login_required(login_url='user:login')
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'title': 'Course Detail',
        'is_course_detail': True,
        'course': course
    }
    return render(request, 'learning/pages/course_detail.html', context=context)
