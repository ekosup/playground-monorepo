import uuid

from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        salt = uuid.uuid4().hex[:6]
        self.slug = self.title.replace(" ", "-").lower() + salt
        super(Notes, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
