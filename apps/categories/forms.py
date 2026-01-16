from django import forms
from .models import ProductCategories

class ProductCategoryForm(forms.ModelForm):
	class Meta:
		model = ProductCategories
		fields = ['name', 'description']