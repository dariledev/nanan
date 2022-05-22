from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from .models import Postes, User, Demandeur, Comment



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'is_homme', 'is_femme')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="nom d'utilisateur", help_text="Champ Obligatoire")
    password = forms.CharField(max_length=63, label="mot de passe", widget=forms.PasswordInput)



class PosteForm(forms.ModelForm):
    class Meta:
        model = Postes
        fields = '__all__'

class DemanderForm(forms.ModelForm):
    class Meta:
        model = Demandeur
        fields = '__all__'


from .models import Comment
  
class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = Comment
        fields =['content']