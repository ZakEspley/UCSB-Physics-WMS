from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from datetimewidget.widgets import DateTimeWidget
from django.forms.models import modelform_factory
from django.urls import reverse_lazy, reverse
from django import forms

from django.core import serializers
from django.db import models
from django.template import loader

from .models import Item, Location, Class, State, Tag, Group, Room
from .forms import ItemForm, LocationForm, ClassForm, StateForm, TagForm, GroupForm, RoomForm

import inflect

p = inflect.engine()
# Create your views here.

################################################################################################
#     Below is the first way I made the views using a decorator to provide the views with
#     arguments, and to generalize them. I found that the class views were simplier
#     so I switched to those but I am keeping this as a comment for an example.
#
# def list_maker(obj, columns, title=None):
#     """
#     Wrapper function that wraps view in HTTP Response for displaying a table of all instances of obj in the database
#     :param obj: Model to be displayed
#     :param columns: I list of heading for the columns that correlate to the fields you want to display in the table.
#     :param title: This is the header that will be used to label the table. If left blank, the title default to the
#                     name of the object pluralized.
#     :return: Returns aa rendered HTTPResponse.
#
#     The context argument is used in the inventory/lists.html file to create the table, and in the base.html file to
#     select the active navigation bar.
#     """
#     if title is None:
#         title = p.plural(obj.__name__)
#
#     def list_decorator(func):
#         def wrapper(request):
#             object_list = obj.objects.order_by('name')
#             context = {
#                 'object_list': object_list,
#                 'columns': columns,
#                 'active': obj.__name__.lower(),
#                 'title': title
#             }
#             return render(request, "inventory/lists2.html", context)
#         return wrapper
#     return list_decorator


# @list_maker(Room, ['name', 'description', 'number'])
# def rooms(request):
#     pass


def index(request):
    return render(request, 'inventory/index.html', {'active': "home"})


class GenericDetailView(DetailView):
    template_name = "detail.html"
    model = Item
    columns = None

    def get_context_data(self, **kwargs):
        context = super(GenericDetailView, self).get_context_data(**kwargs)
        if self.columns is None:
            self.columns = []
            temp = self.model._meta.get_fields()
            for c in temp:
                self.columns.append(str(c).split(".")[-1])
        context['columns'] = self.columns
        context['active'] = self.model.__name__.lower()
        return context


class GenericListView(ListView):
    model = Item
    template_name = "lists.html"
    columns = None
    title = None

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data(**kwargs)
        context['columns'] = self.columns
        if self.title is None:
            self.title = p.plural(self.model.__name__)
        context['title'] = self.title
        context['active'] = self.model.__name__.lower()
        return context


class GenericUpdateView(UpdateView):
    model = Item
    widgets = {'checkout_date': DateTimeWidget(usel10n=True, bootstrap_version=3),
               'checkin_date': DateTimeWidget(usel10n=True, bootstrap_version=3),
               'tags': forms.widgets.CheckboxSelectMultiple(),
               'classes': forms.widgets.CheckboxSelectMultiple()}
    template_name = 'inventory/update.html'
    fields = '__all__'
    columns = None
    title = None

    def get_context_data(self, **kwargs):
        context = super(GenericUpdateView, self).get_context_data(**kwargs)
        context['columns'] = self.columns
        context['title'] = self.title
        context['active'] = self.model.__name__.lower()
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.model.__name__.lower()+"_detail", pk= self.object.id)

    def get_form_class(self):
        return modelform_factory(self.model, fields="__all__", widgets=self.widgets)


class GenericDeleteView(DeleteView):
    model = Item
    template_name = "inventory/delete.html"

    def get_success_url(self):
        return reverse_lazy(self.model.__name__.lower()+"s")


class GenericCreateView(CreateView):
    model = Item
    widgets = {'checkout_date': DateTimeWidget(usel10n=True, bootstrap_version=3),
               'checkin_date': DateTimeWidget(usel10n=True, bootstrap_version=3),
               'tags': forms.widgets.CheckboxSelectMultiple(),
               'classes': forms.widgets.CheckboxSelectMultiple()}
    template_name = 'inventory/new_object.html'
    fields = '__all__'
    columns = None
    title = None

    def get_context_data(self, **kwargs):
        context = super(GenericCreateView, self).get_context_data(**kwargs)
        context['columns'] = self.columns
        if self.title is None:
            self.title = "Add New {0}".format(self.model.__name__)
        context['title'] = self.title
        context['active'] = self.model.__name__.lower()
        return context

    def get_success_url(self):
        return reverse(self.model.__name__.lower()+"_detail", kwargs={'pk': self.object.pk})

    def get_form_class(self):
        print(self.model)
        return modelform_factory(self.model, fields="__all__", widgets=self.widgets)