from django import forms
from .models import Movie,Comment

class SearchForm(forms.ModelForm):
    # class Meta:
    #     model = Movie
    #     fields = ['name',]
    word = forms.CharField(label="Movie Name",max_length=30)
    
# class SearchForm(forms.ModelForm):
#     word = forms.CharField(label='Search Movie')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['content',]