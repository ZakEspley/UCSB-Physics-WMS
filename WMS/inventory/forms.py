from django import forms
from .models import Item

class ItemForm(forms.ModelForm):


    class Meta:
        model = Item
        fields = ('name', 'description','barcode', 'location', 'state', 'tags', 'classes', 'group')
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}
