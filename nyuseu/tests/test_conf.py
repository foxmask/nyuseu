# coding: utf-8
from django.conf import settings
from django.test import TestCase


class NyuseuSettingsTestCase(TestCase):

    """
      check that all the needed config is present
    """

    def test_get_config_service(self):
        self.assertIs(type(settings.BYPASS_BOZO), bool)
