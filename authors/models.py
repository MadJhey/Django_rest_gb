from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)


class Article(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)
