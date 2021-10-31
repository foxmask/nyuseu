# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from django.contrib import admin
from nyuseu.models import Articles, Feeds, Folders, MyBoardFeeds, MyBoard


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'feeds', 'date_created', 'read')
    search_fields = ['title', 'feeds__title']


class FeedsAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'url', 'date_grabbed', 'status')
    search_fields = ['title', 'url', 'folder__title']


class FoldersAdmin(admin.ModelAdmin):
    ordering = ['title']


class MyBoardAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class MyBoardFeedsAdmin(admin.ModelAdmin):
    list_display = ('board', 'feeds')
    search_fields = ['feeds', 'boards__name']


admin.site.register(Feeds, FeedsAdmin)
admin.site.register(Folders, FoldersAdmin)
admin.site.register(Articles, ArticlesAdmin)

admin.site.register(MyBoard, MyBoardAdmin)
admin.site.register(MyBoardFeeds, MyBoardFeedsAdmin)
