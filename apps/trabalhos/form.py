from django import forms
from .models import Trabalho

class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Trabalho
        fields = "__all__"
