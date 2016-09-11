from django import forms
from .models import Item, Group, State, Tag, Class, Location, Room


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description','barcode', 'location', 'state', 'tags', 'classes', 'group')
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = "__all__"
