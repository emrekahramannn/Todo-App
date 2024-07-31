from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Category(models.Model):
    # id
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'category_slug': self.slug,
            }
        )



class Tag(models.Model):
    # id
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'tag',
            kwargs={
                'tag_slug': self.slug,
            }
        )

class Todo(models.Model):
    # id
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'todo_detail',
            kwargs={
                'category_slug': self.category.slug,
                'id': self.id
            }
        )