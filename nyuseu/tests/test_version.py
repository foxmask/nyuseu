# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""
from django.test import TestCase
import nyuseu
import os


class NyuseuVersionTestCase(TestCase):

    """
      check VERSION.txt
    """

    def test_version(self):
        assert os.path.isfile('VERSION.txt')
        self.assertIs(type(nyuseu.__version__), str)
