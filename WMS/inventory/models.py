from django.db import models
from django import forms

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()
    sublocation = models.ForeignKey("self", blank=True, null=True)

    def __str__(self):
        if self.sublocation is None:
            return self.name
        else:
            return str(self.sublocation) + " > " + self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class Item(models.Model):
    barcode = models.PositiveIntegerField()
    location = models.ForeignKey(Location)
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)
    description = models.CharField(max_length=140)
    tags = models.ForeignKey(Tag)
    classes = models.ForeignKey(Class)
    checkout_date = models.DateTimeField('check out date', blank=True, null=True)
    checkin_date = models.DateTimeField('check in date', blank=True, null=True)

    def __str__(self):
        return self.name