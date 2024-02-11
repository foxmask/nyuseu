# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""

from django.apps import AppConfig


class NyuseuConfig(AppConfig):
    """
    let's define the Project Properties
    """
    name = 'nyuseu'
    verbose_name = "Nyuseu :: News :: 뉴스"
    default_auto_field = 'django.db.models.AutoField'
