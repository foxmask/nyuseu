from django.test import TestCase
from nyuseu.models import Articles, Feeds, Folders


class FoldersTest(TestCase):

    """
        Folders Model
    """

    def create_folders(self):

        return Folders(title="FolderA")

    def test_folders(self):
        inst = self.create_folders()
        self.assertTrue(isinstance(inst, Folders))
        self.assertEqual(inst.__str__(), inst.title)


class FeedsTest(TestCase):

    """
        Feeds Model
    """

    def create_feeds(self):

        folder = Folders(title="FolderB")

        title = 'Le Free de la passion'
        url = 'https://foxmask.github.io/feeds/all.atom.xml'
        status = True

        return Feeds(folder=folder, title=title, url=url, status=status)

    def test_feeds(self):
        inst = self.create_feeds()
        self.assertTrue(isinstance(inst, Feeds))
        self.assertEqual(inst.__str__(), inst.title)


class ArticlesTest(TestCase):

    """
        Articles Model
    """

    def create_articles(self):

        folder = Folders(title="FolderC")

        title = 'Le Free de la passion'
        url = 'https://foxmask.github.io/feeds/all.atom.xml'
        status = True

        feeds = Feeds(folder=folder, title=title, url=url, status=status)

        title = 'TEST TITLE'
        image = ''
        text = 'TEST'
        read = False
        return Articles(feeds=feeds, title=title, image=image, text=text, read=read)

    def test_articles(self):
        inst = self.create_articles()
        self.assertTrue(isinstance(inst, Articles))
        self.assertEqual(inst.__str__(), inst.title)
