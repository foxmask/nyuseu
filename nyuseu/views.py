# coding: utf-8
"""
   Nyuseu - 뉴스 - Views
"""
from django.contrib import messages
from django.db.models import Count, Case, When, IntegerField
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from nyuseu.models import Articles, Folders, Feeds


def marked_as_read(request, article_id):
    """

    """
    Articles.objects.filter(id=article_id).update(read=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as read')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def marked_as_unread(request, article_id):
    """

    """
    Articles.objects.filter(id=article_id).update(read=False)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as unread')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def read_later(request, article_id):
    """

    """
    Articles.objects.filter(id=article_id).update(read_later=True, read=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article added to the read later list')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def unread_later(request, article_id):
    """

    """
    Articles.objects.filter(id=article_id).update(read_later=False, read=False)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article removed to the read later list')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


class FoldersMixin:

    def get_context_data(self, *, object_list=None, **kwargs):
        # get only the unread articles of the folders
        folders = Folders.objects.annotate(
            unread=Count(Case(When(feeds__articles__read=False, then=1), output_field=IntegerField()))
        )
        context = super(FoldersMixin, self).get_context_data(**kwargs)
        context['folders'] = folders

        return context


class ArticlesListView(FoldersMixin, ListView):

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

        page_size = self.paginate_by
        context_object_name = self.get_context_object_name(queryset)

        context = super(ArticlesListView, self).get_context_data(**kwargs)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context['paginator'] = paginator
            context['page_obj'] = page
            context['is_paginated'] = is_paginated
            context['object_list'] = queryset
            context['feeds_title'] = feeds_title
        else:
            context['paginator'] = None
            context['page_obj'] = None
            context['is_paginated'] = False
            context['object_list'] = queryset
            context['feeds_title'] = feeds_title

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context


class ArticlesDetailView(FoldersMixin, DetailView):

    model = Articles

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            # update the status "read" to True
            Articles.objects.filter(id=self.object.id).update(read=True)
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)
