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
        mark an article as read
    """
    Articles.objects.filter(id=article_id).update(read=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as <strong>read</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def marked_as_unread(request, article_id):
    """
        mark an article as unread
    """
    Articles.objects.filter(id=article_id).update(read=False)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as <strong>unread</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def read_later(request, article_id):
    """
        mark an article as to read it later
    """
    Articles.objects.filter(id=article_id).update(read_later=True, read=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article <strong>added</strong> '
                                                 'to the <i>read later</i> list')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def unread_later(request, article_id):
    """
        unmark an article as to read it later
    """
    Articles.objects.filter(id=article_id).update(read_later=False, read=False)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article <strong>removed</strong> '
                                                 'to the <i>read later</i> list')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


class FoldersMixin:
    """
        mixin Folders to get all the Folders on the menu_left.html template
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        # get only the unread articles of the folders
        folders = Folders.objects.annotate(
            unread=Count(Case(When(feeds__articles__read=False, then=1), output_field=IntegerField()))
        )
        context = super(FoldersMixin, self).get_context_data(**kwargs)
        context['folders'] = folders

        return context


class FoldersListView(FoldersMixin, ListView):
    """
        Folders List
    """

    model = Articles.articles.unreads()
    paginate_by = 9
    ordering = ['-date_created']
    template_name = 'nyuseu/articles_list.html'

    def get_queryset(self):
        return Articles.articles.unreads()

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        page_size = self.paginate_by
        context_object_name = self.get_context_object_name(queryset)

        context = super(FoldersListView, self).get_context_data(**kwargs)

        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        context['object_list'] = queryset

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context


class ArticlesTinyListView(FoldersMixin, ListView):
    """
        Article List : Multiboard
    """

    # model = Feeds
    queryset = Feeds.objects.filter(status=True)   # get the unread articles
    ordering = ['-date_grabbed']
    template_name = 'nyuseu/articles_list_board.html'


class ArticlesMixin:

    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        feeds_title = ''
        feeds_id = 0
        if 'feeds' in self.kwargs:
            queryset = queryset.filter(feeds=self.kwargs['feeds'])
            feeds = Feeds.objects.filter(id=self.kwargs['feeds'])
            feeds_title = feeds[0].title
            feeds_id = feeds[0].id

        page_size = self.paginate_by
        context_object_name = self.get_context_object_name(queryset)

        context = super(ArticlesMixin, self).get_context_data(**kwargs)

        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        context['object_list'] = queryset
        context['feeds_title'] = feeds_title
        context['feeds_id'] = feeds_id

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context


class ArticlesListView(FoldersMixin, ArticlesMixin, ListView):
    """
        Articles List
    """

    queryset = Articles.articles.unreads()   # get the unread articles
    paginate_by = 9
    ordering = ['-date_created']

    def get_queryset(self):
        return Articles.articles.unreads()


class ArticlesReadListView(FoldersMixin, ArticlesMixin, ListView):
    """
        Articles List already 'Read'
    """

    queryset = Articles.articles.reads()   # get the unread articles
    paginate_by = 9
    ordering = ['-date_created']

    def get_queryset(self):
        return Articles.articles.reads()


class ArticlesDetailView(FoldersMixin, DetailView):
    """
        Articles Details
    """

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
