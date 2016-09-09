from django.shortcuts import render, redirect
from django.template import loader

from .models import Item, Location, Class, State, Tag, Group
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.order_by("name")
    location_list = Location.objects.order_by("name")
    class_list = Class.objects.order_by("name")
    state_list = State.objects.order_by("name")
    tag_list = Tag.objects.order_by("name")
    group_list = Group.objects.order_by("name")
    context = {
        'item_list': item_list,
        'location_list': location_list,
        'class_list': class_list,
        'state_list': state_list,
        'tag_list': tag_list,
        'group_list': group_list,
    }
    return render(request, 'inventory/index.html', context)


def item_new(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_new')
    else:
        return render(request, 'inventory/new_item.html', {'form': form})
