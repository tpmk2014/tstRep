from django import forms
from products.models import Product

class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa produktu', required=True)
    caloric_content = forms.CharField(label="Wartość kaloryczna na 100g ", required=True)

class CaloriesForm(forms.Form):
    name = forms.CharField(label='Nazwa produktu', required=True)
    caloric_content = forms.CharField(label="Wartość kaloryczna na 100g ", required=True)