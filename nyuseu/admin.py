# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from django.contrib import admin
from nyuseu.models import Articles, Feeds, Folders


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'feeds', 'date_created', 'read')
    search_fields = ['title', 'feeds__title']


class FeedsAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'url', 'date_grabbed', 'status')
    search_fields = ['title', 'url', 'folder__title']


class FoldersAdmin(admin.ModelAdmin):
    ordering = ['title']


admin.site.register(Feeds, FeedsAdmin)
admin.site.register(Folders, FoldersAdmin)
admin.site.register(Articles, ArticlesAdmin)
