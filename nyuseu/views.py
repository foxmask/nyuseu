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


def marked_as_read_later(request, article_id):
    """
        mark an article as to be read later
    """
    Articles.objects.filter(id=article_id).update(read_later=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as <strong>to be read later</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def feed_marked_as_read(request, feeds_id):
    """
        mark a complete feed as read
    """
    Articles.objects.filter(feeds__id=feeds_id).update(read=True)
    messages.add_message(request, messages.INFO, 'All articles marked as <strong>read</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[feeds_id]))


def folders_marked_as_read(request, folders):
    """
        mark a complete folder as read
    """
    Articles.objects.filter(feeds__folder__id=folders).update(read=True)
    messages.add_message(request, messages.INFO, 'All articles of that folder marked as <strong>read</strong>')
    return HttpResponseRedirect(reverse('folders', args=[folders]))


def marked_as_read(request, article_id):
    """
        mark an article as read
    """
    Articles.objects.filter(id=article_id).update(read=True)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as <strong>read</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def feed_marked_as_unread(request, feeds_id):
    """
        mark a complete feed as unread
    """
    Articles.objects.filter(feeds__id=feeds_id).update(read=False)
    messages.add_message(request, messages.INFO, 'All articles marked as <strong>unread</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[feeds_id]))


def marked_as_unread(request, article_id):
    """
        mark an article as unread
    """
    Articles.objects.filter(id=article_id).update(read=False)
    article = Articles.objects.get(id=article_id)
    messages.add_message(request, messages.INFO, 'Article marked as <strong>unread</strong>')
    return HttpResponseRedirect(reverse('feeds', args=[article.feeds.id]))


def folders_marked_as_unread(request, folders):
    """
        mark a complete folder as read
    """
    Articles.objects.filter(feeds__folder__id=folders).update(read=False)
    messages.add_message(request, messages.INFO, 'All articles of that folder marked as <strong>unread</strong>')
    return HttpResponseRedirect(reverse('folders', args=[folders]))


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
    return HttpResponseRedirect(reverse('later'))


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

        folders_title = ''
        folders_id = 0
        if 'folders' in self.kwargs:
            queryset = queryset.filter(feeds__folder__id=self.kwargs['folders'])
            feeds = Feeds.objects.filter(folder=self.kwargs['folders'])
            folders_title = feeds[0].folder.title
            folders_id = feeds[0].folder.id

        context = super(FoldersListView, self).get_context_data(**kwargs)

        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        context['object_list'] = queryset
        context['folders_title'] = folders_title
        context['folders_id'] = folders_id

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context


class ArticlesTinyListView(FoldersMixin, ListView):
    """
        Article List : Multiboard
    """

    # queryset = Feeds.objects.filter(status=True).order_by('title')  # get the unread articles
    queryset = Feeds.feeds.multiboard().order_by('title')  # get the unread articles
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

        folders_title = ''
        folders_id = 0
        if 'folders' in self.kwargs:
            queryset = queryset.filter(feeds__folder__id=self.kwargs['folders'])
            feeds = Feeds.objects.filter(folder=self.kwargs['folders'])
            folders_title = feeds[0].folder.title
            folders_id = feeds[0].folder.id

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
        context['folders_title'] = folders_title
        context['folders_id'] = folders_id

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)

        return context


class ArticlesReadLaterListView(FoldersMixin, ArticlesMixin, ListView):
    """
        List of 'ReadLater' Articles
    """

    queryset = Articles.articles.read_later()   # get the unread articles
    ordering = ['-date_created']


class ArticlesListView(FoldersMixin, ArticlesMixin, ListView):
    """
        List of 'Unread' Articles
    """

    queryset = Articles.articles.unreads()   # get the unread articles
    ordering = ['-date_created']


class ArticlesReadListView(FoldersMixin, ArticlesMixin, ListView):
    """
        List of already 'Read' Articles
    """

    queryset = Articles.articles.reads()   # get the read articles
    ordering = ['-date_created']


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
