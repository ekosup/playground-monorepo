from django.shortcuts import render


def home(request):
    context = dict(
        show_footer=True
    )
    return render(request, 'asset/pages/home.html', context)
