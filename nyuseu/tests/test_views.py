from django.test import RequestFactory, TestCase

from nyuseu.views import ArticlesView


class ArticlesViewTestCase(TestCase):

    def setUp(self):
        super(ArticlesViewTestCase, self).setUp()
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_all_articles_list(self):
        template = "index.html"
        # Setup request and view.
        request = RequestFactory().get('/')
        view = ArticlesView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "index.html")

    def test_articles_from_one_feeds(self):
        template = "index.html"
        # Setup request and view.
        request = RequestFactory().get('/articles/10/')
        view = ArticlesView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "index.html")

    def test_articles_page_one(self):
        template = "index.html"
        # Setup request and view.
        request = RequestFactory().get('/?page=1')
        view = ArticlesView.as_view(template_name=template)
        # Run.
        response = view(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "index.html")
