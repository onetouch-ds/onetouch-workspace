from django import forms
from .models import SuggestOther

class SuggestOtherForm(forms.ModelForm):
    class Meta:
        Model = SuggestOther
        fields = ['title','writer', 'content']