from django.contrib import admin
from nyuseu.models import Articles, Feeds, Folders


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'feeds', 'date_created', 'read')
    search_fields = ['title', 'feeds']


class FeedsAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'url', 'date_grabbed')
    search_fields = ['title', 'folder', 'url']


class FoldersAdmin(admin.ModelAdmin):
    ordering = ['title']


admin.site.register(Feeds, FeedsAdmin)
admin.site.register(Folders, FoldersAdmin)
admin.site.register(Articles, ArticlesAdmin)
