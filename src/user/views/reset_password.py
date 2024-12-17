from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages

from user.forms.reset_password import ResetPasswordForm


@login_required
def reset_password(request):
    template_name = 'user/reset-password.html'
    if request.method == 'POST':
        form = ResetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            messages.success(request, 'Password anda berhasil diubah, silakan login kembali.')
            return redirect('home')
        else:
            messages.error(request, 'Silakan perbaiki kesalahan berikut.')
    else:
        form = ResetPasswordForm(request.user)
    return render(request, template_name, {'form': form})
