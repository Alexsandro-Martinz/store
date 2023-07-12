from django import forms

class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    category_id = forms.IntegerField()
    expire_date = forms.CharField(max_length=30)
    units = forms.IntegerField()