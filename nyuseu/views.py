# coding: utf-8
"""
   Nyuseu - 뉴스 - Views
"""
from django.views.generic import ListView
from nyuseu.models import Articles, Folders


class ArticlesView(ListView):
    template_name = 'index.html'
    model = Articles
    ordering = ['-date_created']

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""

        queryset = object_list if object_list is not None else self.object_list
        if 'feeds' in self.kwargs:
            queryset = queryset.filter(feeds=self.kwargs['feeds'])
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        folders = Folders.objects.all()
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
                'folders': folders
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super().get_context_data(**context)