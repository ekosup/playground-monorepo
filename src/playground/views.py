import traceback

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def home(request):
    context = dict(
        show_footer=True
    )
    return render(request, 'asset/pages/home.html', context)


@require_http_methods(["GET"])
def test_storage_connection(request):
    try:
        # Attempt to list files
        files = default_storage.listdir('/')

        # Upload test file
        test_file_path = 'test_connection.txt'
        default_storage.save(test_file_path, b'Connection Test')

        # Get file URL
        file_url = default_storage.url(test_file_path)

        # Delete test file
        default_storage.delete(test_file_path)

        return JsonResponse({
            'status': 'success',
            'files': files,
            'test_file_url': file_url
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e),
            'traceback': traceback.format_exc()
        }, status=500)
