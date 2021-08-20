# coding: utf-8
from django.core.management import call_command
from django.test import TestCase
from io import StringIO


class NyuseuUpdateTestCase(TestCase):

    """
        Running nyuseu_update command
    """

    def test_go(self):

        out = StringIO()
        # call_command('nyuseu_update', stdout=out)
        # print(out.getvalue())
        # self.assertIn('Nyuseu Server Engine - 뉴스 - Feeds Reader Server - Finished!', out.getvalue())
