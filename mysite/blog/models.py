from django.conf import settings
from django.db import models
from django.utils import timezone


# class for posts of website
class Post(models.Model):
    objects = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        :DESCRIPTION: function for publishing posts by declaring actual time and saving post
        """
        self.published_date = timezone.now()
        self.save()

    # function for showing item name in db
    def __str__(self):
        return self.title
