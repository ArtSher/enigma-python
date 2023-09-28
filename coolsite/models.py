from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    AUTHOR_CHOICES = (
        ('ML', 'Machine Learning'),
        ('Web', 'Web Development'),
        ('Syntax', 'Programming Syntax'),
        ('Book', 'Book Reviews'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10, choices=AUTHOR_CHOICES, default='Syntax')
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='images/', default='default_image.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
