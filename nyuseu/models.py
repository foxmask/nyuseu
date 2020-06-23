# coding: utf-8
"""
   Nyuseu - 뉴스 - Models
"""
import datetime
from django.db import models


class Folders(models.Model):

    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name_plural = "Folders"

    def __str__(self):
        return self.title


class Feeds(models.Model):

    folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    url = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=datetime.datetime.now)
    date_grabbed = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Feeds"

    def __str__(self):
        return self.title


class ArticlesQS(models.QuerySet):

    def unreads(self):
        return self.filter(read=False)


class ArticlesUnreadManager(models.Manager):
    """
    get the unread articles
    """
    def get_queryset(self):
        return ArticlesQS(self.model, using=self._db)  # Important!

    def unreads(self):
        return self.get_queryset().unreads()


class Articles(models.Model):

    feeds = models.ForeignKey(Feeds, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.TextField()
    text = models.TextField()
    source_url = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    read_later = models.BooleanField(default=False)

    unreads = ArticlesUnreadManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
