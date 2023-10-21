from django.db import models
from django.conf import settings
from django.urls import reverse
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
    img = models.ImageField(upload_to='images/', default='images/default_image.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True, unique=True, max_length=100)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('post_by_tag', kwargs={'tag_slug': self.slug})
