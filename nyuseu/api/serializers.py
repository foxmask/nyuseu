# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from nyuseu.models import Folders, Feeds, Articles

from rest_framework import serializers


class FeedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feeds
        fields = '__all__'


class FoldersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folders
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = '__all__'
