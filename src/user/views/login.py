from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Username', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label="Password", strip=False, widget=forms.PasswordInput(
            attrs={"autocomplete": "off", 'placeholder': 'Password'}),
    )


class CustomLoginView(LoginView):
    form_class = LoginForm
    next_page = 'home'
    template_name = 'user/account-login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Username atau password salah, silakan coba lagi.')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Anda berhasil login.')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Anda sudah login.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
