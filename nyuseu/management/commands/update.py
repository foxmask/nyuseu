# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from django.core.management.base import BaseCommand

from nyuseu.engine import go

from rich.console import Console

__author__ = 'FoxMaSk'

console = Console()


class Command(BaseCommand):
    """
    command to grab any RSS Feeds and spread them to any available services
    """
    help = 'Update News into \'Nyuseu :: 뉴스 :: News\''

    def handle(self, *args, **options):
        go()
