from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


class Command(BaseCommand):
    help = 'Test storage upload capabilities'

    def handle(self, *args, **kwargs):
        try:
            # Generate test file
            test_content = b"Storage upload test"
            test_path = 'debug/storage_test.txt'

            # Save to storage
            saved_path = default_storage.save(test_path, ContentFile(test_content))

            # Get file URL
            file_url = default_storage.url(saved_path)

            self.stdout.write(self.style.SUCCESS(f"Test file saved: {saved_path}"))
            self.stdout.write(self.style.SUCCESS(f"File URL: {file_url}"))

            # List files
            files = default_storage.listdir('debug')
            self.stdout.write(f"Files in debug directory: {files}")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Storage upload test failed: {e}"))
            import traceback
            traceback.print_exc()