from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='secret99_0'
        )

        self.post = Post.objects.create(
            title='New Post22',
            text='New post and his text',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A good title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'New Post22')
        self.assertEqual(self.post.text, 'New post and his text')
        self.assertEqual(self.post.author, self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse('coolsite:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coolsite/index.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/5/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'coolsite/post_detail.html')
        self.assertContains(response, 'New Post22')

    def test_post_create_view(self):
        response = self.client.post(reverse('coolsite:post_new'), {
            'title': 'New title',
            'text': 'New post text',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New post text')

    def test_post_update_view(self):
        response = self.client.post(reverse('coolsite:post_edit', args='1'), {
            'title': 'Title update',
            'text': 'Text update'
        })
        self.assertEqual(response.status_code, 302)


