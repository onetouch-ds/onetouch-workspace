from django import forms 
from .models import SuggestOther, SuggestVote

class SuggestOtherForm(forms.ModelForm):

    class Meta:
        model = SuggestOther
        fields = ['sgother_pk','sgother_title','sgother_writer','sgother_content']

        widgets={
            'sgother_title': forms.TextInput(
                attrs={'class':'form-control','style':'width:100%'}
            ),
             'sgother_writer': forms.TextInput(
                attrs={'class':'form-control','style':'width:100%'}
            ),
            'sgother_content': forms.Textarea(
                attrs={'class':'form-control','style':'width:100%'}
            ),

        }

class SuggestVoteForm(forms.ModelForm):

    class Meta:
        model = SuggestVote
        fields = ['sgvote_pk','sgvote_title','sgvote_writer','sgvote_content']

        widgets={
            'sgvote_title': forms.TextInput(
                attrs={'class':'form-control','style':'width:100%'}
            ),
             'sgvote_writer': forms.TextInput(
                attrs={'class':'form-control','style':'width:100%'}
            ),
            'sgvote_content': forms.Textarea(
                attrs={'class':'form-control','style':'width:100%'}
            ),

        }        