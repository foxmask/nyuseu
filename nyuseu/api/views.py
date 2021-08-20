# coding: utf-8
"""
Nyuseu - News - 뉴스
"""
from nyuseu.api.serializers import ArticlesSerializer, FeedsSerializer, FoldersSerializer

from nyuseu.models import Articles, Feeds, Folders

from rest_framework import viewsets


class ArticlesViewSet(viewsets.ModelViewSet):
    """
        ViewSet for listing or retrieving articles
        available methods are
        /GET .list(), .retrieve(),
        /POST .create(),
        /UPDATE .update(),
        /PATCH .partial_update(), and
        /DELETE .destroy()
    """
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()


class FeedsViewSet(viewsets.ModelViewSet):
    """
        ViewSet for listing or retrieving Feeds
        available methods are
        /GET .list(), .retrieve(),
        /POST .create(),
        /UPDATE .update(),
        /PATCH .partial_update(), and
        /DELETE .destroy()
    """
    serializer_class = FeedsSerializer
    queryset = Feeds.objects.all()


class FoldersViewSet(viewsets.ModelViewSet):
    """
        ViewSet for listing or retrieving Folders
        available methods are
        /GET .list(), .retrieve(),
        /POST .create(),
        /UPDATE .update(),
        /PATCH .partial_update(), and
        /DELETE .destroy()
    """
    serializer_class = FoldersSerializer
    queryset = Folders.objects.all()
