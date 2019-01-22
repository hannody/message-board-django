from django.db import models

# Create your models here.


class Post(models.Model):
    #title = models.TextField(default="Enter a title here")

    text = models.TextField(default="Enter text here")

    def __str__(self):
        return self.text[:50]
