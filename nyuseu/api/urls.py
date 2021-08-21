# coding: utf-8
"""
Nyuseu - News - 뉴스
"""
from django.urls import include, path
from django.views.generic import TemplateView
from nyuseu.api.views import ArticlesViewSet, FeedsViewSet, FoldersViewSet
from rest_framework import routers
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'feeds', FeedsViewSet)
router.register(r'folders', FoldersViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v2/', include(router.urls)),

    # API DOC - begin
    path('v1/swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('v1/openapi', get_schema_view(
        title="Nyuseu - News - 뉴스",
        description="Nyuseu API",
        version="0.2.0"
    ), name='openapi-schema'),
    # API DOC - end
]
