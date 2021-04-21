from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=25, null=False)
    isbn = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title