from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    external_id = models.IntegerField(unique=True, null=True, blank=True) # For 3rd party API

    def __str__(self):
        return self.title