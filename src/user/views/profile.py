from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import User


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
