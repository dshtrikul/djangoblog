from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# python manage.py sqlmigrate blog 0001

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='post_pics')

    def get_absolute_url(self):
        return reverse('blog-home')
