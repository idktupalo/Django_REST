from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=121)
    isbn = models.CharField(max_length=13) # ISBN is a unique, 13-character identifier assigned to every published book

    def __str__(self):
        return self.title