# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:27:28 2016

@author: Zach
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index)
]