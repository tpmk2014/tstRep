from django import forms

class ProductForm(forms.Form):
    name = forms.EmailField(label='Nazwa produktu', required=True)
    caloric_content = forms.CharField(label="Wartość kaloryczna na 100g ", required=True)