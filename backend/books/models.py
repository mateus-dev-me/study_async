from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tag)
    file = models.FileField(upload_to='books')

    def __str__(self):
        return self.title


class ViewBook(models.Model):
    ip = models.GenericIPAddressField()
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ip
