from django.test import TestCase
from .models import Post, Comment

from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):

        self.post = Post.objects.create(
            title="Test Post", content="This is a test content", author="Test Author"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author, "Test Author")

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")


class CommentModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Sample Post", content="Sample Content", author="Sample Author"
        )

        self.comment = Comment.objects.create(
            post=self.post, author="Commenter", text="This is a comment"
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.text, "This is a comment")


class PostAPITest(APITestCase):
    def setUp(self):

        # self.user = User.objects.create_user(username="testuser", password="password123")
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.post = Post.objects.create(
            title="API Test Post", content="Testing Post Content", author="Test Author"
        )

    def test_list_posts(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        response = self.client.get(f"/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "API Test Post")

    def test_creating_post(self):
        data = {"title": "new post", "content": "new content", "author": "new author"}
        response = self.client.get("/posts/add/", data)
        print("retrieve post by id : ", status)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post(self):
        data = {
            "title": "updated title",
            "content": "updated content",
            "author": "updated author",
        }
        response = self.client.put(
            f"/posts/change/{self.post.id}/", data, format="json"
        )
        print("update status code : ", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_post(self):
        response = self.client.get(f"/posts/remove/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CommentAPITest(APITestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post for Comments", content="Post content", author="Author"
        )

        self.comment = Comment.objects.create(
            post=self.post, author="Commentor", text="Test comment"
        )

    def test_list_comments(self):
        response = self.client.get("/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        comment = {"author": "new commentor", "text": "new comment text"}
        response = self.client.get("/comments/add/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
