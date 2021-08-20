# coding: utf-8
from django.test import TestCase
import nyuseu
import os


class NyuseuSettingsTestCase(TestCase):

    """
      check VERSION.txt
    """

    def test_version(self):
        assert os.path.isfile('VERSION.txt')
        self.assertIs(type(nyuseu.__version__), str)
