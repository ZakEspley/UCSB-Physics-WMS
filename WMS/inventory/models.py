from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.


class IterModel(object):

    def __iter__(self):
        for i in vars(self):
            if i == "id" or i.startswith("_"):
                continue
            elif i.endswith('id'):
                i = i.replace("_id", '_set')
                yield (i, getattr(self, str(i)))

            else:
                yield (i, getattr(self, str(i)))


# class IterModel2(object):
#
#     def __iter__(self):
#         for field_name in self._meta.get_fields():
#             value = getattr(self, field_name, None)
#             return (field_name, value)

class Group(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField(blank=True, null=True)
    room = models.ForeignKey("Room")

    def __str__(self):
        return str(self.room) + " > " + self.name


class State(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Class(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Item(models.Model):
    barcode = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, blank=True, null=True)
    description = models.CharField(max_length=140)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    classes = models.ManyToManyField(Class, blank=True, null=True)
    checkout_date = models.DateTimeField('check out date', blank=True, null=True)
    checkin_date = models.DateTimeField('check in date', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})

    def do_prefix(self, name, prefix):
        if prefix:
            return "%s.%s" % (prefix, name)
        return name

    def get_fields_flat(self):
        return [name for name in self]

    def __iter__(self):
        fields = self._meta.fields
        for field in fields:
            name = self.do_prefix(field.attname, None)
            yield name
            if field.rel:
                rel = field.rel.to
                for f in rel:
                    yield f


class Room(models.Model, IterModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    number = models.PositiveIntegerField()
    barcode = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name