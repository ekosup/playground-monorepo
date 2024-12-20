from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """
    Storage untuk integrasi file media ke S3 compatible file storage
    - bila ada file dengan nama sama, maka beri suffix agar tidak overwrite
    - menggunakan mekanisme pre-signed url
    - url expired setelah 10 menit
    """
    bucket_name = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', 'media')
    file_overwrite = False
    querystring_auth = True
    querystring_expire = 600
    default_acl = 'private'
    base_location = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', 'media')
