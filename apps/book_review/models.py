from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models

# Create your models here.

class AuthorManager(models.Manager):

    def check_name(self, name):
        if len(name) < 2:
            return False
        return True

    def check_exists(self, name):
        if Author.objects.filter(name=name).exists():
            return True
        return False

class BookManager(models.Manager):

    def check_name(self, title):
        if len(title) < 2:
            return False
        return True

    def check_exists(self, title):
        if Book.objects.filter(title=title).exists():
            return True
        return False

class ReviewManager(models.Manager):

    def check_review(self, review):
        if len(review) < 2:
            return False
        return True

class Author(models.Model):
    name = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()

class Review(models.Model):
    review = models.CharField(max_length = 355)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ReviewManager()
