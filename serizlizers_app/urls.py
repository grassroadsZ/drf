# -*- encoding:utf-8 -*-
"""
@Author: grassroadsZ
@data: 2020/6/4 15:29
@file: urls.py

"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^snippets/$', views.serizlizerapp_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.serizlizerapp_detail),

]
