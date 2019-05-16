from django import forms
from .models import Movie,Comment,Score

class SearchForm(forms.ModelForm):
    # class Meta:
    #     model = Movie
    #     fields = ['name',]
    word = forms.CharField(label="Movie Name",max_length=30)
    

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        # comment만 입력받기
        fields = ['content',]
        
