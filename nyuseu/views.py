# coding: utf-8
"""
   Nyuseu - 뉴스 - Views
"""
from django.db.models import Count, Case, When, IntegerField
from django.views.generic import ListView

from nyuseu.models import Articles, Folders, Feeds


class ArticlesView(ListView):
    template_name = 'index.html'
    queryset = Articles.unreads   # get the unread articles
    paginate_by = 9
    ordering = ['-date_created']

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        feeds_title = ''
        if 'feeds' in self.kwargs:
            queryset = queryset.filter(feeds=self.kwargs['feeds'])
            feeds = Feeds.objects.filter(id=self.kwargs['feeds'])
            feeds_title = feeds[0].title

        # get only the unread articles of the folders
        folders = Folders.objects.annotate(
            unread=Count(Case(When(feeds__articles__read=False, then=1), output_field=IntegerField()))
        )

        page_size = self.paginate_by
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset,
                'feeds_title': feeds_title,
                'folders': folders
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
                'feeds_title': feeds_title,
                'folders': folders
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context
