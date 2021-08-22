# coding: utf-8
"""
Nyuseu :: News :: 뉴스
"""
from django.urls import include, path
from django.views.generic import TemplateView
import nyuseu
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
    path('v1/doc/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('v1/openapi', get_schema_view(
        title="Nyuseu :: 뉴스 :: News - API",
        description="<h2>Description</h2><br/>This is the complete API to deal with <a href=\"https://gitlab.com/annyong/nyuseu\">'Nyuseu :: 뉴스 :: News'</a> data<br/><h2>Help</h2><br/> You can find out help on <a href=\"https://framateam.org/annyong/channels/town-square\">the Mattermost instance</a>",
        version=nyuseu.__version__
    ), name='openapi-schema'),
    # API DOC - end
]
