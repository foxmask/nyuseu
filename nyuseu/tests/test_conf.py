# coding: utf-8
import unittest
from django.conf import settings


class NyuseuSettingsTestCase(unittest.TestCase):

    """
      check that all the needed config is present
    """

    def test_get_config_service(self):
        self.assertIs(type(settings.BYPASS_BOZO), bool)
