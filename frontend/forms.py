from django import forms

class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=50)
    description = forms.TextInput()
    category_id = forms.IntegerField()
    expire_date = forms.DateField()
    units = forms.IntegerField()
    