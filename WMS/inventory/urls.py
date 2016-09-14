# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:27:28 2016

@author: Zak
"""

from django.conf.urls import url
from .models import Item, Location, Group, State, Tag, Class, Room

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^items/new$', views.GenericCreateView.as_view(model=Item), name='new_item'),
    url(r'^locations/new$', views.GenericCreateView.as_view(model=Location), name='new_location'),
    url(r'^groups/new$', views.GenericCreateView.as_view(model=Group), name='new_group'),
    url(r'^classes/new$', views.GenericCreateView.as_view(model=Class), name='new_class'),
    url(r'^states/new$', views.GenericCreateView.as_view(model=State), name='new_state'),
    url(r'^tags/new$', views.GenericCreateView.as_view(model=Tag), name='new_tag'),
    url(r'^rooms/new', views.GenericCreateView.as_view(model=Room), name="new_room"),

    url(r'^items/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=Item), name='update_item'),
    url(r'^locations/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=Location), name='update_location'),
    url(r'^groups/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=Group), name='update_group'),
    url(r'^classes/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=Class), name='update_class'),
    url(r'^states/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=State), name='update_state'),
    url(r'^tags/(?P<pk>[0-9]+)/update$', views.GenericUpdateView.as_view(model=Tag), name='update_tag'),
    url(r'^rooms/(?P<pk>[0-9]+)/update', views.GenericUpdateView.as_view(model=Room), name="update_room"),

    url(r'^items/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=Item), name='delete_item'),
    url(r'^locations/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=Location), name='delete_location'),
    url(r'^groups/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=Group), name='delete_group'),
    url(r'^classes/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=Class), name='delete_class'),
    url(r'^states/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=State), name='delete_state'),
    url(r'^tags/(?P<pk>[0-9]+)/delete$', views.GenericDeleteView.as_view(model=Tag), name='delete_tag'),
    url(r'^rooms/(?P<pk>[0-9]+)/delete', views.GenericDeleteView.as_view(model=Room), name="delete_room"),

    url(r'^items$', views.GenericListView.as_view(columns=['name', 'description', 'location', 'state']), name='items'),
    url(r'^locations$', views.GenericListView.as_view(model=Location, columns=['name', 'description', 'room']), name='locations'),
    url(r'^groups$',  views.GenericListView.as_view(model=Group, columns=['name', 'description']), name='groups'),
    url(r'^classes$', views.GenericListView.as_view(model=Class, columns=['name', 'description']), name='classes'),
    url(r'^states$', views.GenericListView.as_view(model=State, columns=['name', 'description']), name='states'),
    url(r'^tags$', views.GenericListView.as_view(model=Tag, columns=['name', 'description']), name='tags'),
    url(r"^rooms$", views.GenericListView.as_view(model=Room, columns=['name', 'description', 'number']), name='rooms'),

    url(r"^items/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Item, columns=['name','description','group', 'location', 'state', 'tags', 'classes', 'checkin_date', "checkout_date", 'barcode']), name='item_detail'),
    url(r"^locations/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Location, columns=['name', 'description', 'room', 'barcode']), name='location_detail'),
    url(r"^groups/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Group, columns=['name', 'description', 'barcode']), name='group_detail'),
    url(r"^states/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=State, columns=['name', 'description', 'barcode']), name='state_detail'),
    url(r"^tags/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Tag, columns=['name', 'description', 'barcode']), name='tag_detail'),
    url(r"^classes/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Class, columns=['name', 'description']), name='class_detail'),
    url(r"^rooms/(?P<pk>[0-9]+)/$", views.GenericDetailView.as_view(model=Room, columns=['name', 'description', 'number', 'barcode']), name='room_detail')
]