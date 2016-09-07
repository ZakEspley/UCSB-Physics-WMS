from django.shortcuts import render
from django.template import loader

from .models import Item

# Create your views here.

def index(request):
    item_list = Item.objects.order_by("name")
    context = {
        'item_list': item_list
    }
    return render(request, 'inventory/index.html', context)

