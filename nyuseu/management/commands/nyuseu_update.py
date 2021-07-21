# coding: utf-8
"""
Nyuseu - News - 뉴스
"""

from django.core.management.base import BaseCommand

from nyuseu.engine import go

__author__ = 'FoxMaSk'


class Command(BaseCommand):

    def handle(self, *args, **options):
        go()
