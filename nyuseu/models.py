# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from django.db import models
from django.db.models import UniqueConstraint
import django.utils.timezone


class Folders(models.Model):
    """
        Folders Model
    """

    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        verbose_name_plural = "Folders"

    def __str__(self):
        return self.title


class FeedsQS(models.QuerySet):
    """
        QuerySet
    """

    def multiboard(self):
        return self.filter(multiboard=True)


class FeedsManager(models.Manager):
    """
        Manager to get the feed for the multiboard
    """
    def get_queryset(self):
        return FeedsQS(self.model, using=self._db)  # Important!

    def multiboard(self):
        return self.get_queryset().multiboard()


class Feeds(models.Model):
    """
        Feeds Model
    """

    folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    url = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=django.utils.timezone.now)
    date_grabbed = models.DateTimeField(default=django.utils.timezone.now)
    status = models.BooleanField(default=True)
    multiboard = models.BooleanField(default=True)

    feeds = FeedsManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Feeds"

    def __str__(self):
        return self.title


class ArticlesQS(models.QuerySet):
    """
        QuerySet
    """

    def reads(self):
        return self.filter(read=True)

    def unreads(self):
        return self.filter(read=False).order_by('-date_created')

    def read_later(self):
        return self.filter(read_later=True).order_by('-date_created')


class ArticlesManager(models.Manager):
    """
        Manager to get the (un)read articles
    """
    def get_queryset(self):
        return ArticlesQS(self.model, using=self._db)  # Important!

    def reads(self):
        return self.get_queryset().reads()

    def unreads(self):
        return self.get_queryset().unreads()

    def read_later(self):
        return self.get_queryset().read_later()


class Articles(models.Model):
    """
        Articles Model
    """

    feeds = models.ForeignKey(Feeds, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.TextField()
    text = models.TextField()
    source_url = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    read_later = models.BooleanField(default=False)

    articles = ArticlesManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Articles"
        constraints = [
            UniqueConstraint(fields=['feeds', 'title', ], name='unique_article')
        ]

    def __str__(self):
        return self.title


class MyBoard(models.Model):
    """
        MyBoard Model
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MyBoardFeeds(models.Model):
    """
        MyBoard Model
    """
    board = models.ForeignKey(MyBoard, on_delete=models.CASCADE)
    feeds = models.ForeignKey(Feeds, on_delete=models.CASCADE)
