# coding: utf-8
from django.core import management
from django.test import TestCase
from nyuseu.models import Articles, Folders, Feeds


class TestCmdMgt(TestCase):

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

    def test_run_nyuseu(self):
        self.create_stuff()
        management.call_command('nyuseu', verbosity=0)

    def test_run_nyuseu2(self):
        article = self.create_stuff()
        management.call_command('nyuseu', f"-id={article.id}", verbosity=0)

    def test_run_nyuseu_update(self):
        self.create_stuff()
        management.call_command('nyuseu_update', verbosity=0)

    def test_run_opml_export(self):
        self.create_stuff()
        management.call_command('opml_export', 'sample/foobar.opml', verbosity=0)

    def test_run_opml_export2(self):
        management.call_command('opml_export', 'sample/foobar', verbosity=0)

    def test_run_opml_load(self):
        opml_file = 'sample/feedly-e2343e92-9e71-4345-b045-cef7e1736cd2-2020-06-20.opml'
        management.call_command('opml_load', opml_file, verbosity=0)

    def test_run_opml_load2(self):
        opml_file = 'sample/feedly-e2343e92-9e71-4345-b045-cef7e1736cd2-2020-06-20'
        management.call_command('opml_load', opml_file, verbosity=0)
