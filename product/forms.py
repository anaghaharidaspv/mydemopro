from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'status']



class ExcelForm(forms.Form):
    file = forms.FileField(label='Select an Excel file')


# forms.py



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'discount']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Set the product field as a hidden field so it gets submitted properly
        self.fields['product'].widget = forms.HiddenInput()
