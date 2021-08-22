# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""
from django.conf import settings
from django.test import TestCase
import os


class NyuseuSettingsTestCase(TestCase):

    """
      check that all the needed config is present
    """

    def test_env_file(self):
        assert os.path.isfile('nyuseu/.env')

    def test_get_config_service(self):
        self.assertIs(type(settings.BYPASS_BOZO), bool)
        self.assertIs(type(settings.LANGUAGE_CODE), str)
        self.assertIs(type(settings.TIME_ZONE), str)
        self.assertIs(type(settings.USE_L10N), bool)
        self.assertIs(type(settings.USE_TZ), bool)
        self.assertIs(type(settings.ALLOWED_HOSTS), list)
        self.assertIs(type(settings.SECRET_KEY), str)
