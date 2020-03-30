from django.db import models
from django.utils import timezone


class Topics(models.Model):
    title = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)
    published_date = models.CharField(max_length=100,null=True)
    author = models.TextField(null=True)
    topic_url = models.TextField(max_length=100, null=True)
    image_url = models.TextField(null=True)
    top_news = models.CharField(max_length=8, null=True)
    domain_tags = models.TextField()

    def publish(self):
        self.upload_date = timezone.now()

        self.save()

    def __str__(self):
        return self.title

    def __str__(self):
        return self.description

    def __str__(self):
        return self.published_date

    def __str__(self):
        return self.author

    def __str__(self):
        return self.image_url

    def __str__(self):
        return self.domain_tags



# Create your models here.
