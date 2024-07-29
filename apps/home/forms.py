from django import forms
from django.contrib.auth.models import User
from .models import Category, Subcategory, Element, Data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['title', 'element_type', 'category', 'subcategory']

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['value']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'class': 'form-control'})
