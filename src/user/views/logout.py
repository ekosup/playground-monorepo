from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import View


class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Anda berhasil logout. Sampai jumpa lagi!')
        return redirect('user:login')