from django import forms
from .models import Product, ProductImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean

        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]

        if len(result) > 5:
            raise forms.ValidationError("Máximo 5 imágenes por producto")

        return result

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

class CreateProductForm(ProductForm):
    images = MultipleFileField()

