"""nyuseu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from nyuseu.views import (ArticlesListView, ArticlesDetailView,
                          read_later, unread_later, marked_as_read, marked_as_unread)

urlpatterns = [
    path('', ArticlesListView.as_view(), name="home"),
    path('feeds/<int:feeds>/', ArticlesListView.as_view(), name="feeds"),
    path('articles/<int:pk>/', ArticlesDetailView.as_view(), name="articles"),
    path('articles/read_later/<int:article_id>/', read_later, name="read_later"),
    path('articles/unread_later/<int:article_id>/', unread_later, name="unread_later"),
    path('articles/marked_as_read/<int:article_id>/', marked_as_read, name="marked_as_read"),
    path('articles/marked_as_unread/<int:article_id>/', marked_as_unread, name="marked_as_unread"),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
