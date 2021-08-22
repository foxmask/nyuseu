# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""
from django.test import RequestFactory, TestCase
from django.contrib.messages.storage.fallback import FallbackStorage

from nyuseu.models import Feeds, Folders, Articles
from nyuseu.views import FoldersListView, ArticlesListView, ArticlesDetailView
from nyuseu.views import marked_as_read, marked_as_unread, read_later, unread_later


class FoldersListViewTestCase(TestCase):

    def create_folder(self):
        return Folders.objects.create(title="FolderX")

    def setUp(self):
        super(FoldersListViewTestCase, self).setUp()
        self.factory = RequestFactory()

    def test_articleslist_for_folder(self):
        folder = self.create_folder()
        template = "nyuseu/articles_list.html"
        # Setup request and view.
        request = RequestFactory().get(f'/folders/{folder.id}')
        view = FoldersListView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "nyuseu/articles_list.html")


class ArticlesListViewTestCase(TestCase):

    def create_stuff(self):
        folder = Folders.objects.create(title="FolderD")
        title = 'Le Free de la passion'
        url = 'https://foxmask.github.io/feeds/all.atom.xml'
        status = True

        feeds = Feeds.objects.create(folder=folder, title=title, url=url, status=status)
        title = 'TEST TITLE'
        image = ''
        text = 'TEST'
        read = False
        Articles.objects.create(feeds=feeds, title=title, image=image, text=text, read=read)
        return feeds

    def setUp(self):
        super(ArticlesListViewTestCase, self).setUp()
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_all_articles_list(self):
        template = "nyuseu/articles_list.html"
        # Setup request and view.
        request = RequestFactory().get('/')
        view = ArticlesListView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "nyuseu/articles_list.html")

    def test_articles_list_from_feeds(self):
        feeds = self.create_stuff()
        template = "nyuseu/articles_list.html"
        # Setup request and view.
        request = RequestFactory().get(f'/feeds/{feeds.id}/')
        kwargs = {'feeds': feeds.id}
        view = ArticlesListView.as_view(template_name=template)(request, **kwargs)
        # Run.
        # response = view(request)
        # Check.
        self.assertEqual(view.status_code, 200)
        self.assertEqual(view.template_name[0], "nyuseu/articles_list.html")

    def test_articles_list_no_page_size(self):
        feeds = self.create_stuff()
        template = "nyuseu/articles_list.html"
        # Setup request and view.
        request = RequestFactory().get(f'/feeds/{feeds.id}/')
        kwargs = {'feeds': feeds.id}
        view = ArticlesListView.as_view(template_name=template)(request, **kwargs)
        # Run.
        # response = view(request)
        # Check.
        self.assertEqual(view.status_code, 200)
        self.assertEqual(view.template_name[0], "nyuseu/articles_list.html")

    def test_articles_page_one(self):
        template = "nyuseu/articles_list.html"
        # Setup request and view.
        request = RequestFactory().get('/?page=1')
        view = ArticlesListView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "nyuseu/articles_list.html")


class ArticlesDetailViewTestCase(TestCase):

    def create_articles(self):
        folder = Folders.objects.create(title="FolderC")
        title = 'Le Free de la passion'
        url = 'https://foxmask.github.io/feeds/all.atom.xml'
        status = True

        feeds = Feeds.objects.create(folder=folder, title=title, url=url, status=status)
        title = 'TEST TITLE'
        image = ''
        text = 'TEST'
        read = False
        article = Articles.objects.create(feeds=feeds, title=title, image=image, text=text, read=read)
        return article

    def setUp(self):
        super(ArticlesDetailViewTestCase, self).setUp()
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_articles_detail(self):
        article = self.create_articles()
        template = "nyuseu/articles_detail.html"
        # Setup request and view.
        request = RequestFactory().get(f'articles/{article.id}/')
        view = ArticlesDetailView.as_view(template_name=template)
        # Run.
        response = view(request, pk=article.id)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "nyuseu/articles_detail.html")


class ViewFunction(TestCase):

    def create_articles(self):
        folder = Folders.objects.create(title="FolderC")
        title = 'Le Free de la passion'
        url = 'https://foxmask.github.io/feeds/all.atom.xml'
        status = True

        feeds = Feeds.objects.create(folder=folder, title=title, url=url, status=status)
        title = 'TEST TITLE'
        image = ''
        text = 'TEST'
        read = False
        article = Articles.objects.create(feeds=feeds, title=title, image=image, text=text, read=read)
        return article

    def setUp(self):
        super(ViewFunction, self).setUp()
        self.request = RequestFactory().get('/')

    def test_marked_as_read(self):
        article = self.create_articles()
        # Setup request and view.
        setattr(self.request, 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)
        response = marked_as_read(request=self.request, article_id=article.id)

        # Check.
        self.assertEqual(response.status_code, 302)

    def test_marked_as_unread(self):
        article = self.create_articles()
        # Setup request and view.
        setattr(self.request, 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)
        response = marked_as_unread(request=self.request, article_id=article.id)

        # Check.
        self.assertEqual(response.status_code, 302)

    def test_read_later(self):
        article = self.create_articles()
        # Setup request and view.
        setattr(self.request, 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)
        response = read_later(request=self.request, article_id=article.id)

        # Check.
        self.assertEqual(response.status_code, 302)

    def test_unread_later(self):
        article = self.create_articles()
        # Setup request and view.
        setattr(self.request, 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)
        response = unread_later(request=self.request, article_id=article.id)

        # Check.
        self.assertEqual(response.status_code, 302)
