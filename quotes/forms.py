from django import forms
from . models import Quote,QuoteCategory
from django.forms import ModelForm

class CreateForm(ModelForm):
    class Meta:
        model=Quote
        exclude=['author','id']
        labels={
            'quote':'Write quote: ',
            'categories':'Select quote Category: '
        }
        help_texts = {
            'categories': 'control+click for selecting multiple category',

        }

# class editForm(forms.Form):
#     new_quote=forms.CharField(label='Modify the quote:',widget=forms.Textarea)
#     new_category=forms.ModelMultipleChoiceField(label='Select the categories:', queryset=QuoteCategory.objects.all(), help_text="control+click for selecting multiple category")

class editForm(ModelForm):   
    class Meta:
        model=Quote
        exclude=['author','id']

        labels={
            'quote':'Write quote: ',
            'categories':'Select quote Category: '
        }
        help_texts = {
            'categories': 'control+click for selecting multiple category',

        }
        
    