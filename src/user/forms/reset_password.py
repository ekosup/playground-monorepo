from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _


class ResetPasswordForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': _('Password lama salah. Silakan coba lagi.'),
        'password_mismatch': _('Password yang dimasukkan tidak sama'),
    }

    old_password = forms.CharField(
        label=_("Password sebelumnya"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'off',
                'class': 'py-2 px-4 leading-6 block w-full border border-gray-300 rounded text-sm focus:border-gray-300 focus:ring-0',
                'placeholder': 'Password sebelumnya'}
        )
    )
    new_password1 = forms.CharField(
        label=_("Password baru"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'off',
                'class': 'py-2 px-4 leading-6 block w-full border border-gray-300 rounded text-sm focus:border-gray-300 focus:ring-0',
                'placeholder': 'Password baru'}
        )
    )
    new_password2 = forms.CharField(
        label=_("Ulangi password baru"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'off',
                'class': 'py-2 px-4 leading-6 block w-full border border-gray-300 rounded text-sm focus:border-gray-300 focus:ring-0',
                'placeholder': 'Ulangi password baru'}
        )
    )
