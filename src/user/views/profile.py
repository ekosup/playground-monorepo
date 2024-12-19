import os

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView

from user.models import User, UserProfile


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user/profile.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    extra_context = {'title': 'Profile'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object().profile
        context['is_profile'] = True
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect('user:profile', username=self.get_object().username)

    def dispatch(self, request, *args, **kwargs):
        try:
            self.get_object().profile
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=request.user)
        return super().dispatch(request, *args, **kwargs)


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']


def post_profile_picture(request, *args, **kwargs):
    form = ProfilePictureForm(request.POST, request.FILES)
    if form.is_valid():
        profile = request.user.profile
        profile_pic = form.cleaned_data['profile_pic']

        # Rename the file using user.id
        file_extension = os.path.splitext(profile_pic.name)[1]
        new_file_name = f"user-{request.user.id}-pic{file_extension}"
        new_file_path = os.path.join('profile_pics', new_file_name)

        # Save the file to the new path
        saved_path = default_storage.save(new_file_path, ContentFile(profile_pic.read()))

        # Update the profile picture path
        profile.profile_pic = saved_path
        profile.save()
        return JsonResponse({'status': 'success'})
    return HttpResponseBadRequest(form.errors.as_json(), content_type='application/json')
