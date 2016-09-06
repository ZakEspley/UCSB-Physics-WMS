from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()

class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()


class State(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    barcode = models.PositiveIntegerField()


class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)

class Item(models.Model):
    barcode = models.PositiveIntegerField()
    location = models.ForeignKey(Location)
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)
    description = models.CharField(max_length=140)
    tags = models.ForeignKey(Tag)
    classes = models.ForeignKey(Class)
    checkout_date = models.DateTimeField('check out date')
    checkin_date = models.DateTimeField('check in date')