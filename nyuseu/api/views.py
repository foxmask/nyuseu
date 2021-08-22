# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""
from nyuseu.api.serializers import ArticlesSerializer, FeedsSerializer, FoldersSerializer
from nyuseu.models import Articles, Feeds, Folders

from rest_framework import viewsets


class ArticlesViewSet(viewsets.ModelViewSet):
    """
        ViewSet for creating, updating, listing, retrieving, deleting articles
    """
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()


class FeedsViewSet(viewsets.ModelViewSet):
    """
        ViewSet for creating, updating, listing, retrieving, deleting Feeds
    """
    serializer_class = FeedsSerializer
    queryset = Feeds.objects.all()


class FoldersViewSet(viewsets.ModelViewSet):
    """
        ViewSet for creating, updating, listing, retrieving, deleting Folders
    """
    serializer_class = FoldersSerializer
    queryset = Folders.objects.all()
