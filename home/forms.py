from django.forms import ModelForm
from .models import Writter,Post

class NewWritterForm(ModelForm):
    class Meta:
        model = Writter
        fields = '__all__'

class NewPoemForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'