# coding: utf-8
"""
Nyuseu - News - 뉴스
"""
from django.urls import include, path
from rest_framework import routers
from nyuseu.api.views import ArticlesViewSet, FeedsViewSet, FoldersViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'feeds', FeedsViewSet)
router.register(r'folders', FoldersViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v2/', include(router.urls)),

]
