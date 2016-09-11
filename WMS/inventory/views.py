from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.db import models
from django.template import loader

from .models import Item, Location, Class, State, Tag, Group, Room
from .forms import ItemForm, LocationForm, ClassForm, StateForm, TagForm, GroupForm, RoomForm

import inflect

p = inflect.engine()
# Create your views here.

def object_maker(obj, title=None):

    def obj_decorator(func):

        def wrapper(request):
            form = obj()
            if request.method == "POST":
                form = obj(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('new_'+obj.__name__.replace('Form', "").lower())
            else:
                return render(request, 'inventory/new_object.html', {'form': form, "title": title})

        return wrapper

    return obj_decorator

def list_maker(obj, columns, title=None):
    """
    Wrapper function that wraps view in HTTP Response for displaying a table of all instances of obj in the database
    :param obj: Model to be displayed
    :param columns: I list of heading for the columns that correlate to the fields you want to display in the table.
    :param title: This is the header that will be used to label the table. If left blank, the title default to the
                    name of the object pluralized.
    :return: Returns aa rendered HTTPResponse.

    The context argument is used in the inventory/lists.html file to create the table, and in the base.html file to
    select the active navigation bar.
    """
    if title is None:
        title = p.plural(obj.__name__)

    def list_decorator(func):
        def wrapper(request):
            object_list = obj.objects.order_by('name')
            context = {
                'object_list': object_list,
                'columns': columns,
                'active': obj.__name__.lower(),
                'title': title
            }
            return render(request, "inventory/lists2.html", context)
        return wrapper
    return list_decorator


def index(request):
    return render(request, 'inventory/index.html', {'active': "home"})


@object_maker(ItemForm, "New Item")
def new_item(request):
    pass


@object_maker(GroupForm, "New Group")
def new_group(request):
    pass


@object_maker(TagForm, "New Tag")
def new_tag(request):
    pass


@object_maker(LocationForm, "New Location")
def new_location(request):
    pass


@object_maker(StateForm, "New State")
def new_state(request):
    pass


@object_maker(ClassForm, "New Class")
def new_class(request):
    pass

@object_maker(RoomForm, "New Room")
def new_room(request):
    pass


@list_maker(Item, ['name', 'description', 'location', 'state'], "Items in Stock")
def items(request):
    pass


@list_maker(Location, ['name', 'description', 'room'])
def locations(request):
    pass


@list_maker(Group, ['name', 'description'], "Item Groups")
def groups(request):
    pass


@list_maker(Class, ['name', 'description'])
def classes(request):
    pass


@list_maker(Tag, ['name', 'description'])
def tags(request):
    pass


@list_maker(State, ['name', 'description'])
def states(request):
    pass


@list_maker(Room, ['name', 'description', 'number'])
def rooms(request):
    pass


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

