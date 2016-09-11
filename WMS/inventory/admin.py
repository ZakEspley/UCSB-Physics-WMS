from django.contrib import admin

# Register your models here.

from .models import Item, Group, Tag, Location, State, Class, Room

admin.site.register(Item)
admin.site.register(Group)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(State)
admin.site.register(Class)
admin.site.register(Room)
