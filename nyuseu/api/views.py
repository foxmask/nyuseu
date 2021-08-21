# coding: utf-8
"""
Nyuseu - News - 뉴스
"""
from nyuseu.api.serializers import ArticlesSerializer, FeedsSerializer, FoldersSerializer
from nyuseu.models import Articles, Feeds, Folders

from rest_framework import viewsets, status
from rest_framework.response import Response


class ArticlesViewSet(viewsets.ModelViewSet):
    """
        ViewSet for creating, updating, listing, retrieving, deleting articles
    """
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()

    def create(self, request, *args, **kwargs):
        feeds_str = request.data['feeds']
        feeds = Feeds.objects.get(title=feeds_str)
        request.data['feeds'] = feeds.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        feeds_str = request.data['feeds']
        feeds = Feeds.objects.get(title=feeds_str)
        request.data['feeds'] = feeds.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


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
