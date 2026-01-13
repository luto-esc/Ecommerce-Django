from django import forms
from .models import Product, ProductImage

'''
--> ClereableFileinput is Django's widget for file fields, defines how
the <input type='file'> looks and behaves in HTML, when you use
django generate a input: select a file, shows the file already uploaded (if it exist), allows you to delete it (not save nothing, only shows)
'''
class MultipleFileInput(forms.ClearableFileInput):
#Add support for multiple files
    allow_multiple_selected = True


'''
Creating a new fieldform that behaves like a FileField
inherit--> file validations, manage request.FiLES, errors django's 
'''
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):

        #kwargs--> dict whit field configurations
        #.setdefault say "if no one has passed a widget, use this on by default"   
        #this field ever use <input type='file' multiple>
        #->in conclusion the browser send list of fileds

        kwargs.setdefault("widget", MultipleFileInput())
       

        #super().__init__(*args, **kwargs)-->internally, django
        #Save the widget, registers the fild, config validators
        #handles errors, prepare clean()
        super().__init__(*args, **kwargs)

#--> The clean method
#receives the raw data (from the html), validates it, trasforms it,
#returns the clean data, or launch an error
#->clean() runs automatically when you do form.is_valid()


#--> Parameters
#-> data -> this is what comes from the browser
#-> initial -> this initial field value (used in editing) 

    def clean(self, data, initial=None):
    #use standard django clean() -> validate an file
        single_file_clean = super().clean

#html whit multiple can return -> list or tuple

#-->case one if: for d in data
#call django's original clean(), validet the file, return clean file, add to result, pass initial for edit 
#--> isintance is a native function python's
# syntax -> isinstance(object, type) ex: isinstance(5,int)->true
#     return -> true or false

        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        #-->case two else: cover list in one element
        else:
            result = [single_file_clean(data, initial)]
            
        if len(result) > 5:
            raise forms.ValidationError("Maximun 5 images for product")
        #-->return a list
        return result

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost_price', 'price', 'stock']

'''
this form have filds of ProductForm, images field (does not belong to the model )
'''
class CreateProductForm(ProductForm):
#-->this adds an extra field to the form
    images = MultipleFileField(required=False)


