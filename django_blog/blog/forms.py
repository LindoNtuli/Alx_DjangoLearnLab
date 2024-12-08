from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment
from django.forms import CheckboxSelectMultiple

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
#end
        
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), 
        widgets=TagWidget(),
        required=False  #optional
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class TagWidget(CheckboxSelectMultiple):
    template_name = 'widgets/tag_widget.html'
    
#end

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
